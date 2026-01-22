import asyncio
import os
import datetime
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import ChatWriteForbiddenError, FloodWaitError

# --- CONFIGURAÇÕES GERAIS ---
API_ID = int(os.environ.get('TELEGRAM_API_ID'))
API_HASH = os.environ.get('TELEGRAM_API_HASH')

# --- LISTA DE ATIRADORES (EXÉRCITO) ---
# Agora cada conta tem seu próprio 'chat_id' e 'msg'
CONTAS = [
    {
        "nome": "Kaique",
        "secret_name": "TELEGRAM_SESSION",
        "chat_id": -4801139096,  # <--- COLOQUE O ID DO GRUPO DO KAIQUE AQUI (Número Inteiro)
        "msg": "Kaique fabio andre raio 3"
    },
    {
        "nome": "Jaqueline", 
        "secret_name": "SESSION_JAQUELINE",
        "chat_id": -4801139096,  # <--- COLOQUE O ID DO GRUPO DA JAQUELINE AQUI
        "msg": "Jaqueline x Daniel raio 3"
    }
]

# ⚠️ AJUSTE AQUI PARA O DIA DA COMPETIÇÃO ⚠️
HORA_ALVO = 17
MINUTO_ALVO = 47

async def sniper_individual(conta, alvo):
    """Função que controla UMA conta específica"""
    
    session_str = os.environ.get(conta['secret_name'])
    
    if not session_str:
        print(f"⚠️ Pulei {conta['nome']}: Segredo '{conta['secret_name']}' não encontrado.")
        return

    client = TelegramClient(StringSession(session_str), API_ID, API_HASH)
    
    # Valida se o chat_id foi preenchido
    chat_alvo_especifico = conta.get('chat_id')
    if not chat_alvo_especifico:
        print(f"❌ {conta['nome']} não tem ID de chat configurado!")
        return

    try:
        await client.connect()
        
        # --- ADICIONE ESTA LINHA AQUI EMBAIXO ---
        # Isso força o robô a atualizar a lista de grupos e "encontrar" o ID
        await client.get_dialogs()  
        # ----------------------------------------

        if not await client.is_user_authorized():
            print(f"❌ {conta['nome']}: Falha no Login (Sessão inválida).")
            return

        print(f"✅ {conta['nome']} logado e pronto para o alvo {chat_alvo_especifico}!")

        # --- FASE 1: ESPERA SINCRONIZADA ---
        while (alvo - datetime.datetime.now()).total_seconds() > 5:
            await asyncio.sleep(1)

        # --- FASE 2: ATAQUE ---
        enviado = False
        tempo_limite = alvo + datetime.timedelta(minutes=2)
        
        while not enviado and datetime.datetime.now() < tempo_limite:
            try:
                # Usa o chat_id específico desta conta
                await client.send_message(chat_alvo_especifico, conta['msg'])
                enviado = True
                print(f"🏆 {conta['nome']} -> ENVIOU! ({datetime.datetime.now().strftime('%H:%M:%S.%f')})")
                
            except ChatWriteForbiddenError:
                await asyncio.sleep(0.2) 
            except FloodWaitError as e:
                print(f"🛑 {conta['nome']} FloodWait: {e.seconds}s")
                await asyncio.sleep(e.seconds)
            except Exception as e:
                print(f"⚠️ {conta['nome']} erro: {e}")
                await asyncio.sleep(0.5)

    except Exception as e:
        print(f"❌ Erro fatal na conta {conta['nome']}: {e}")
    finally:
        await client.disconnect()

async def main():
    agora = datetime.datetime.now()
    alvo = agora.replace(hour=HORA_ALVO, minute=MINUTO_ALVO, second=0, microsecond=0)
    
    print(f"🔥 INICIANDO SNIPER MULTIPLO ({len(CONTAS)} contas)")
    print(f"🎯 Alvo: {alvo.strftime('%H:%M:%S')}")

    while (alvo - datetime.datetime.now()).total_seconds() > 30:
        restante = int((alvo - datetime.datetime.now()).total_seconds())
        if restante % 30 == 0:
            print(f"💤 Aguardando... Falta {restante}s")
        await asyncio.sleep(1)

    print("⚔️ PREPARANDO ATAQUE SIMULTÂNEO... (Faltam < 30s)")
    
    tarefas = []
    for conta in CONTAS:
        tarefas.append(sniper_individual(conta, alvo))
    
    await asyncio.gather(*tarefas)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())