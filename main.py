import asyncio
import os
import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from dotenv import load_dotenv
from telethon import TelegramClient, errors, events, types, utils
from telethon.sessions import StringSession

try:
    import uvloop  # type: ignore
except ImportError:
    uvloop = None


# =========================
# CONFIGURAÇÕES
# =========================

load_dotenv()

API_ID_RAW = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")

if not API_ID_RAW or not API_HASH:
    raise RuntimeError("Defina TELEGRAM_API_ID e TELEGRAM_API_HASH no .env")

API_ID = int(API_ID_RAW)

TIMEZONE = ZoneInfo(os.getenv("BOT_TIMEZONE", "America/Sao_Paulo"))

# Tempo entre tentativas quando o grupo ainda está fechado/restrito.
# 0.030 = 30ms
ATTEMPT_INTERVAL_SEC = float(os.getenv("ATTEMPT_INTERVAL_SEC", "0.030"))

# Tempo máximo que ele fica tentando depois do alvo.
MAX_WINDOW_SEC = float(os.getenv("MAX_WINDOW_SEC", "80.0"))

# Preparação antes do alvo.
WARMUP_BEFORE_SEC = float(os.getenv("WARMUP_BEFORE_SEC", "60.0"))
ALERT_BEFORE_SEC = float(os.getenv("ALERT_BEFORE_SEC", "30.0"))

# Tempo que ele espera por evento de abertura antes de voltar para tentativa normal.
EVENT_WAIT_SEC = float(os.getenv("EVENT_WAIT_SEC", "3.0"))


CONTAS = [
    {
        "nome": "Kaique",
        "secret_name": "SESSION_KAIQUE",
        "chat_id": -4999405862,
        "msg": "ok",
        "hora": 1,
        "minuto": 50,
    },
    {
        "nome": "Laysa",
        "secret_name": "SESSION_LAYSA",
        "chat_id": -4999405862,
        "msg": "Laysa x Mg R5",
        "hora": 1,
        "minuto": 50,
    },
    {
        "nome": "Katia",
        "secret_name": "SESSION_KATIA",
        "chat_id": -5296287589,
        "msg": "Katia pantanal r2 laudo",
        "hora": 1,
        "minuto": 50,
    },
]


@dataclass(frozen=True)
class Mission:
    nome: str
    secret_name: str
    chat_id: int
    msg: str
    target: datetime


# =========================
# LOGS / TEMPO
# =========================

def now() -> datetime:
    return datetime.now(TIMEZONE)


def fmt(dt: datetime | None = None) -> str:
    dt = dt or now()
    return dt.strftime("%H:%M:%S.%f")[:-3]


def log(nome: str, texto: str) -> None:
    print(f"[{fmt()}] [{nome}] {texto}", flush=True)


def build_target(hour: int, minute: int) -> datetime:
    atual = now()
    alvo = atual.replace(hour=hour, minute=minute, second=0, microsecond=0)

    if (atual - alvo).total_seconds() > MAX_WINDOW_SEC:
        alvo += timedelta(days=1)

    return alvo


async def sleep_until(target: datetime, *, alert_name: str | None = None) -> None:
    alert_logged = False

    while True:
        restante = (target - now()).total_seconds()

        if restante <= 0:
            return

        if alert_name and not alert_logged and restante <= ALERT_BEFORE_SEC:
            log(alert_name, f"⚠️ ALERTA MÁXIMO ativado. Faltam {restante:.3f}s para o alvo.")
            alert_logged = True

        if restante > 5:
            await asyncio.sleep(min(1.0, restante - 5))
        elif restante > 1:
            await asyncio.sleep(0.050)
        elif restante > 0.050:
            await asyncio.sleep(0.005)
        else:
            await asyncio.sleep(0)


# =========================
# TELETHON
# =========================

def make_client(session_str: str) -> TelegramClient:
    client = TelegramClient(
        StringSession(session_str),
        API_ID,
        API_HASH,
        request_retries=0,
        connection_retries=2,
        retry_delay=0.2,
        auto_reconnect=True,
        flood_sleep_threshold=0,
        receive_updates=True,
    )
    client.parse_mode = None
    return client


async def prepare_client(client: TelegramClient, mission: Mission):
    await client.connect()

    if not await client.is_user_authorized():
        raise RuntimeError("sessão não autorizada")

    try:
        entity = await client.get_input_entity(mission.chat_id)
    except Exception:
        await client.get_dialogs(limit=200)
        entity = await client.get_input_entity(mission.chat_id)

    return entity


async def wait_group_open_event(
    client: TelegramClient,
    mission: Mission,
    entity,
    deadline_perf: float,
) -> bool:
    opened = asyncio.Event()

    try:
        full_entity = await client.get_entity(entity)
        target_peer_id = utils.get_peer_id(full_entity)
    except Exception:
        target_peer_id = mission.chat_id

    def same_chat(message) -> bool:
        try:
            msg_peer_id = utils.get_peer_id(message.peer_id)
            return msg_peer_id == target_peer_id or msg_peer_id == mission.chat_id
        except Exception:
            return False

    @client.on(events.Raw)
    async def raw_handler(update):
        message = getattr(update, "message", None)

        if not isinstance(message, types.MessageService):
            return

        if not same_chat(message):
            return

        action = getattr(message, "action", None)

        if isinstance(action, types.MessageActionChatEditDefaultBannedRights):
            rights = getattr(action, "default_banned_rights", None)
            send_blocked = getattr(rights, "send_messages", None)

            log(
                mission.nome,
                f"👀 update de permissão detectado | send_messages_bloqueado={send_blocked}"
            )

            if send_blocked is False:
                opened.set()

    try:
        restante = max(0.0, deadline_perf - time.perf_counter())
        await asyncio.wait_for(opened.wait(), timeout=restante)
        return True

    except asyncio.TimeoutError:
        return False

    finally:
        client.remove_event_handler(raw_handler, events.Raw)


async def try_send_once(
    client: TelegramClient,
    mission: Mission,
    entity,
    attempts: int,
    started_perf: float,
    modo: str,
):
    sent = await client.send_message(
        entity,
        mission.msg,
        link_preview=False,
        clear_draft=False,
    )

    sent_at = now()
    elapsed_ms = (time.perf_counter() - started_perf) * 1000

    log(
        mission.nome,
        f"🏆 ENVIOU {modo} em {fmt(sent_at)} | tentativa={attempts} | "
        f"+{elapsed_ms:.1f}ms após alvo | message_id={getattr(sent, 'id', 'n/a')}"
    )


async def run_mission(mission: Mission) -> None:
    session_str = os.getenv(mission.secret_name)

    if not session_str:
        log(mission.nome, f"⚠️ pulado: variável {mission.secret_name} não encontrada no .env")
        return

    client = make_client(session_str)
    warmup_at = mission.target - timedelta(seconds=WARMUP_BEFORE_SEC)

    try:
        log(
            mission.nome,
            f"🎯 alvo travado: {mission.target.strftime('%Y-%m-%d %H:%M:%S')} | chat={mission.chat_id}"
        )

        if warmup_at > now():
            await sleep_until(warmup_at)

        log(mission.nome, "🔌 conectando e aquecendo entidade...")
        entity = await prepare_client(client, mission)
        log(mission.nome, "✅ pronto. entidade resolvida e conexão ativa.")

        await sleep_until(mission.target, alert_name=mission.nome)

        started_at = now()
        started_perf = time.perf_counter()
        deadline_perf = started_perf + MAX_WINDOW_SEC

        log(
            mission.nome,
            f"🚀 janela de disparo aberta em {fmt(started_at)}. Nenhuma tentativa foi feita antes do alvo."
        )

        attempts = 0
        last_error = ""

        # =========================
        # 1) PRIMEIRA TENTATIVA DIRETA
        # =========================
        try:
            attempts += 1
            await try_send_once(
                client=client,
                mission=mission,
                entity=entity,
                attempts=attempts,
                started_perf=started_perf,
                modo="direto",
            )
            return

        except (errors.ChatWriteForbiddenError, errors.ChatSendPlainForbiddenError):
            last_error = "chat fechado/restrito"
            log(mission.nome, "🔒 envio direto falhou: grupo fechado/restrito. Aguardando evento curto...")

        except errors.SlowModeWaitError as e:
            log(mission.nome, f"🛑 SlowModeWaitError: aguarde {e.seconds}s. Parando.")
            return

        except errors.FloodWaitError as e:
            log(mission.nome, f"🛑 FloodWaitError: Telegram pediu {e.seconds}s. Parando.")
            return

        except (errors.UserBannedInChannelError, errors.ChatAdminRequiredError) as e:
            log(mission.nome, f"❌ sem permissão definitiva: {type(e).__name__}. Parando.")
            return

        except Exception as e:
            last_error = type(e).__name__
            log(mission.nome, f"⚠️ envio direto falhou: {type(e).__name__}: {e}")
            log(mission.nome, "👂 aguardando evento curto antes de voltar para tentativa normal...")

        # =========================
        # 2) ESPERA EVENTO POR POUCOS SEGUNDOS
        # =========================
        event_deadline_perf = min(
            deadline_perf,
            time.perf_counter() + EVENT_WAIT_SEC
        )

        opened_by_event = await wait_group_open_event(
            client=client,
            mission=mission,
            entity=entity,
            deadline_perf=event_deadline_perf,
        )

        if opened_by_event:
            detected_at = now()
            detected_ms = (time.perf_counter() - started_perf) * 1000

            log(
                mission.nome,
                f"🟢 abertura detectada por evento em {fmt(detected_at)} | +{detected_ms:.1f}ms após alvo. Enviando..."
            )

            try:
                attempts += 1
                await try_send_once(
                    client=client,
                    mission=mission,
                    entity=entity,
                    attempts=attempts,
                    started_perf=started_perf,
                    modo="por evento",
                )
                return

            except (errors.ChatWriteForbiddenError, errors.ChatSendPlainForbiddenError):
                last_error = "chat fechado/restrito após evento"
                log(mission.nome, "⚠️ evento veio, mas envio ainda falhou. Voltando para tentativa normal...")

            except errors.FloodWaitError as e:
                log(mission.nome, f"🛑 FloodWaitError após evento: Telegram pediu {e.seconds}s. Parando.")
                return

            except Exception as e:
                last_error = type(e).__name__
                log(mission.nome, f"❌ evento detectado, mas envio falhou: {type(e).__name__}: {e}")

        else:
            log(mission.nome, "⏱️ nenhum evento útil detectado. Voltando para tentativa normal...")

        # =========================
        # 3) TENTATIVA NORMAL ATÉ MAX_WINDOW_SEC
        # =========================
        while time.perf_counter() <= deadline_perf:
            attempts += 1

            try:
                await try_send_once(
                    client=client,
                    mission=mission,
                    entity=entity,
                    attempts=attempts,
                    started_perf=started_perf,
                    modo="normal",
                )
                return

            except (errors.ChatWriteForbiddenError, errors.ChatSendPlainForbiddenError):
                last_error = "chat fechado/restrito"
                await asyncio.sleep(ATTEMPT_INTERVAL_SEC)

            except errors.SlowModeWaitError as e:
                log(mission.nome, f"🛑 SlowModeWaitError: aguarde {e.seconds}s. Parando.")
                return

            except errors.FloodWaitError as e:
                log(mission.nome, f"🛑 FloodWaitError: Telegram pediu {e.seconds}s. Parando.")
                return

            except (errors.UserBannedInChannelError, errors.ChatAdminRequiredError) as e:
                log(mission.nome, f"❌ sem permissão definitiva: {type(e).__name__}. Parando.")
                return

            except Exception as e:
                last_error = type(e).__name__
                log(mission.nome, f"⚠️ erro inesperado na tentativa {attempts}: {type(e).__name__}: {e}")
                await asyncio.sleep(max(ATTEMPT_INTERVAL_SEC, 0.040))

        elapsed_ms = (time.perf_counter() - started_perf) * 1000
        log(
            mission.nome,
            f"⏹️ não enviou. tentativas={attempts} | tempo={elapsed_ms:.1f}ms | último_erro={last_error or 'nenhum'}"
        )

    except Exception as e:
        log(mission.nome, f"❌ erro fatal: {type(e).__name__}: {e}")

    finally:
        if client.is_connected():
            await client.disconnect()
            log(mission.nome, "🔌 desconectado.")


def load_missions() -> list[Mission]:
    missions: list[Mission] = []

    for c in CONTAS:
        nome = str(c.get("nome", "")).strip()
        secret_name = str(c.get("secret_name", "")).strip()
        chat_id = c.get("chat_id")
        msg = str(c.get("msg", ""))

        if not nome or not secret_name or not isinstance(chat_id, int) or not msg.strip():
            print(f"[{fmt()}] [CONFIG] ⚠️ conta inválida ignorada: {c}", flush=True)
            continue

        missions.append(
            Mission(
                nome=nome,
                secret_name=secret_name,
                chat_id=chat_id,
                msg=msg,
                target=build_target(int(c["hora"]), int(c["minuto"])),
            )
        )

    by_secret: dict[str, list[str]] = {}

    for m in missions:
        by_secret.setdefault(m.secret_name, []).append(m.nome)

    for secret, nomes in by_secret.items():
        if len(nomes) > 1:
            print(
                f"[{fmt()}] [CONFIG] ⚠️ mesma sessão usada em múltiplas missões: "
                f"{secret} -> {', '.join(nomes)}. Isso pode aumentar flood/limitação.",
                flush=True,
            )

    return missions


async def main() -> None:
    missions = load_missions()

    if not missions:
        print(f"[{fmt()}] [MAIN] nenhuma missão válida.", flush=True)
        return

    print(f"[{fmt()}] [MAIN] 🔥 iniciando {len(missions)} missão(ões)", flush=True)

    for m in missions:
        print(
            f"[{fmt()}] [MAIN] - {m.nome}: {m.target.strftime('%Y-%m-%d %H:%M:%S')} | chat={m.chat_id}",
            flush=True,
        )

    await asyncio.gather(*(run_mission(m) for m in missions))

    print(f"[{fmt()}] [MAIN] ✅ finalizado. Entrando em hibernação.", flush=True)

    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    if uvloop is not None:
        uvloop.install()

    asyncio.run(main())