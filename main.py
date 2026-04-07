import asyncio
import datetime as dt
import os
from dataclasses import dataclass
from zoneinfo import ZoneInfo

from telethon import TelegramClient
from telethon.errors import ChatWriteForbiddenError, FloodWaitError
from telethon.sessions import StringSession


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Variavel de ambiente obrigatoria ausente: {name}")
    return value


API_ID = int(get_required_env("TELEGRAM_API_ID"))
API_HASH = get_required_env("TELEGRAM_API_HASH")
TIMEZONE = ZoneInfo(os.getenv("BOT_TIMEZONE", "America/Sao_Paulo"))

PREPARE_SECONDS = int(os.getenv("PREPARE_SECONDS", "60"))
RETRY_INTERVAL_SECONDS = float(os.getenv("RETRY_INTERVAL_SECONDS", "0.027"))
GIVE_UP_AFTER_SECONDS = int(os.getenv("GIVE_UP_AFTER_SECONDS", "120"))
RUN_FOREVER = os.getenv("RUN_FOREVER", "0").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}


ACCOUNTS = {
    "sara": {
        "secret_name": "SESSION_SARA",
    },

    "Steffani": {
        "secret_name": "SESSION_STEFFANI",
    },

}


JOBS = [
    {
        "name": "sara",
        "account": "sara",
        "hour": 15,
        "minute": 55,
        "weekdays": [1],
        "chat_id": -5215567369,
        "msg": "Sara esposa demorisval raio 1 cela 27 longa distância",
    },

    {
        "name": "Steffani",
        "account": "Steffani",
        "hour": 15,
        "minute": 55,
        "weekdays": [1],
        "chat_id": -5207514700,
        "msg": "Steffani/Gigante R3",
    },
]


@dataclass
class ConnectedAccount:
    name: str
    client: TelegramClient


@dataclass
class PreparedJob:
    job_name: str
    account_name: str
    client: TelegramClient
    chat: object
    msg: str


def now_local() -> dt.datetime:
    return dt.datetime.now(TIMEZONE)


def validate_jobs() -> None:
    if not JOBS:
        raise RuntimeError("Cadastre pelo menos um item em JOBS.")

    for job in JOBS:
        account_name = job["account"]
        if account_name not in ACCOUNTS:
            raise RuntimeError(
                f"Job {job['name']} referencia a conta {account_name}, "
                "mas ela nao existe em ACCOUNTS."
            )


def next_occurrence(job: dict, reference: dt.datetime) -> dt.datetime:
    weekdays = job.get("weekdays")

    for day_offset in range(8):
        candidate_date = reference.date() + dt.timedelta(days=day_offset)
        if weekdays is not None and candidate_date.weekday() not in weekdays:
            continue

        candidate = dt.datetime.combine(
            candidate_date,
            dt.time(job["hour"], job["minute"]),
            tzinfo=TIMEZONE,
        )
        if candidate > reference:
            return candidate

    raise RuntimeError(f"Nao encontrei uma proxima execucao valida para {job['name']}.")


def get_next_job_batch(reference: dt.datetime) -> tuple[list[dict], dt.datetime]:
    candidates = [(job, next_occurrence(job, reference)) for job in JOBS]
    next_target = min(target for _, target in candidates)
    next_jobs = [job for job, target in candidates if target == next_target]
    return next_jobs, next_target


async def sleep_until(target: dt.datetime) -> None:
    while True:
        remaining = (target - now_local()).total_seconds()
        if remaining <= 0:
            return

        if remaining > 300:
            sleep_for = 60
        elif remaining > 60:
            sleep_for = 15
        elif remaining > 5:
            sleep_for = 1
        else:
            sleep_for = min(remaining, 0.05)

        await asyncio.sleep(sleep_for)


async def prepare_account(account_name: str) -> ConnectedAccount | None:
    account = ACCOUNTS[account_name]
    session_str = os.getenv(account["secret_name"])
    if not session_str:
        print(
            f"[SKIP] {account_name}: secret {account['secret_name']} nao encontrado."
        )
        return None

    client = TelegramClient(StringSession(session_str), API_ID, API_HASH)

    try:
        await client.connect()
        if not await client.is_user_authorized():
            print(f"[ERRO] {account_name}: sessao nao autorizada.")
            await client.disconnect()
            return None

        print(f"[OK] {account_name} conectado.")
        return ConnectedAccount(name=account_name, client=client)
    except Exception as exc:
        print(f"[ERRO] {account_name}: falha ao preparar conta: {exc}")
        if client.is_connected():
            await client.disconnect()
        return None


async def prepare_job(job: dict, account: ConnectedAccount) -> PreparedJob | None:
    try:
        input_chat = await account.client.get_input_entity(job["chat_id"])
        print(
            f"[OK] Job {job['name']} armado com a conta {account.name} "
            f"para {job['hour']:02d}:{job['minute']:02d}."
        )
        return PreparedJob(
            job_name=job["name"],
            account_name=account.name,
            client=account.client,
            chat=input_chat,
            msg=job["msg"],
        )
    except Exception as exc:
        print(f"[ERRO] Job {job['name']}: falha ao resolver chat: {exc}")
        return None


async def close_account(account: ConnectedAccount) -> None:
    if account.client.is_connected():
        await account.client.disconnect()


async def send_with_retry(
    job: PreparedJob,
    target: dt.datetime,
    fire_event: asyncio.Event,
) -> bool:
    await fire_event.wait()

    attempts = 0
    while True:
        drift = (now_local() - target).total_seconds()
        if drift > GIVE_UP_AFTER_SECONDS:
            print(f"[TIMEOUT] {job.job_name}: janela esgotada.")
            return False

        try:
            await job.client.send_message(job.chat, job.msg)
            sent_at = now_local()
            delta_ms = int((sent_at - target).total_seconds() * 1000)
            print(
                f"[ENVIO] {job.job_name} ({job.account_name}) "
                f"em {sent_at.strftime('%H:%M:%S.%f')} ({delta_ms:+} ms)"
            )
            return True
        except ChatWriteForbiddenError:
            attempts += 1
            await asyncio.sleep(RETRY_INTERVAL_SECONDS)
        except FloodWaitError as exc:
            print(f"[FLOOD] {job.job_name}: aguardando {exc.seconds}s.")
            await asyncio.sleep(exc.seconds)
        except Exception as exc:
            attempts += 1
            print(f"[WARN] {job.job_name}: tentativa {attempts} falhou: {exc}")
            await asyncio.sleep(0.1)


async def run_job_batch(jobs: list[dict], target: dt.datetime) -> None:
    prepare_at = target - dt.timedelta(seconds=PREPARE_SECONDS)
    now = now_local()
    job_names = ", ".join(job["name"] for job in jobs)

    print(
        f"[AGENDA] {len(jobs)} job(s) -> {target.strftime('%d/%m/%Y %H:%M:%S %Z')} "
        f"| {job_names}"
    )

    if now < prepare_at:
        print(
            f"[ESPERA] Dormindo ate {prepare_at.strftime('%H:%M:%S')} "
            "para preparar as contas."
        )
        await sleep_until(prepare_at)

    account_names = sorted({job["account"] for job in jobs})
    print("[PREP] Conectando contas antes do disparo...")
    connected_accounts = {
        account.name: account
        for account in await asyncio.gather(
            *(prepare_account(account_name) for account_name in account_names)
        )
        if account is not None
    }

    if not connected_accounts:
        print("[ERRO] Nenhuma conta ficou pronta para o lote.")
        return

    prepared_jobs = [
        prepared
        for prepared in await asyncio.gather(
            *(
                prepare_job(job, connected_accounts[job["account"]])
                for job in jobs
                if job["account"] in connected_accounts
            )
        )
        if prepared is not None
    ]

    if not prepared_jobs:
        print("[ERRO] Nenhum job ficou pronto para enviar.")
        await asyncio.gather(*(close_account(account) for account in connected_accounts.values()))
        return

    fire_event = asyncio.Event()
    fire_delay = max((target - now_local()).total_seconds(), 0)
    handle = asyncio.get_running_loop().call_later(fire_delay, fire_event.set)

    print(
        f"[ARMADO] {len(prepared_jobs)} job(s) aguardando o mesmo gatilho para enviar."
    )

    try:
        results = await asyncio.gather(
            *(send_with_retry(job, target, fire_event) for job in prepared_jobs)
        )
        success_count = sum(1 for result in results if result)
        print(f"[FIM] {success_count}/{len(prepared_jobs)} job(s) enviados.")
    finally:
        handle.cancel()
        await asyncio.gather(*(close_account(account) for account in connected_accounts.values()))


async def runner() -> None:
    validate_jobs()

    while True:
        jobs, target = get_next_job_batch(now_local())
        await run_job_batch(jobs, target)

        if not RUN_FOREVER:
            return

        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(runner())
