import asyncio
import os
import datetime
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import ChatWriteForbiddenError, FloodWaitError
from dotenv import load_dotenv

# Carrega os segredos de dentro da Vultr
load_dotenv()

# --- CONFIGURAÇÕES GERAIS ---
API_ID = int(os.environ.get('TELEGRAM_API_ID'))
API_HASH = os.environ.get('TELEGRAM_API_HASH')

# --- LISTA DE ATIRADORES (EXÉRCITO INDEPENDENTE) ---
CONTAS = [
    {
        "nome": "Kaique", 
        "secret_name": "SESSION_KAIQUE",
        "chat_id": -4999405862,
        "msg": "ok",
        "hora": 23,   # <-- Horário individual
        "minuto": 58  # <-- Horário individual
    },  
    {
        "nome": "Laysa", 
        "secret_name": "SESSION_LAYSA",
        "chat_id": -4999405862,
        "msg": "Laysa x Mg R5",
        "hora": 23,
        "minuto": 58
    },  
    {
        "nome": "Katia", 
        "secret_name": "SESSION_KATIA",
        "chat_id": -5296287589,
        "msg": "Katia pantanal r2 laudo",
        "hora": 23,   # Exemplo: Atira mais cedo amanhã
        "minuto": 58
    }
]

async def sniper_individual(conta):
    """Função otimizada para VELOCIDADE MÁXIMA (Modo Turbo)"""
    
    session_str = os.environ.get(conta['secret_name'])
    if not session_str:
        print(f"⚠️ Pulei {conta['nome']}: Segredo não encontrado na Vultr.")
        return

    client = TelegramClient(StringSession(session_str), API_ID, API_HASH)
    chat_alvo_especifico = conta.get('chat_id')

    # Calcula o alvo específico desta conta
    agora = datetime.datetime.now()
    alvo = agora.replace(hour=conta['hora'], minute=conta['minuto'], second=0, microsecond=0)

    # Se a hora alvo já passou hoje, ajusta para atirar amanhã
    if (alvo - agora).total_seconds() < -120:
        alvo += datetime.timedelta(days=1)

    try:
        await client.connect()
        await client.get_dialogs()
        
        if not await client.is_user_authorized():
            print(f"❌ {conta['nome']}: Falha no Login.")
            return

        print(f"✅ {conta['nome']} pronto. Alvo travado para: {alvo.strftime('%H:%M:%S')}")

        # --- FASE 1: ESPERA (Modo Econômico) ---
        while (alvo - datetime.datetime.now()).total_seconds() > 30:
            await asyncio.sleep(1)

        print(f"⚠️ {conta['nome']} entrou em ALERTA MÁXIMO (Faltam < 30s)")

        # --- FASE 2: AQUECIMENTO E DISPARO ---
        enviado = False
        tentativa = 0
        
        while not enviado:
            agora = datetime.datetime.now()
            diferenca = (alvo - agora).total_seconds()

            if diferenca < -120: 
                print(f"❌ {conta['nome']} Desistindo (Tempo esgotado).")
                break

            # TRAVA DE PRECISÃO: Segura o disparo até dar a hora EM PONTO
            if diferenca > 0:
                await asyncio.sleep(0.001)
                continue

            # --- ZONA DE GUERRA (A hora exata chegou) ---
            try:
                await client.send_message(chat_alvo_especifico, conta['msg'])
                
                enviado = True
                print(f"🏆 {conta['nome']} -> ENVIOU! TENTATIVA {tentativa} ({datetime.datetime.now().strftime('%H:%M:%S.%f')})")
                
            except ChatWriteForbiddenError:
                tentativa += 1
                # FREIO DE 40ms: Ideal para servidores em Miami (evita FloodWait)
                await asyncio.sleep(0.040) 
                
            except FloodWaitError as e:
                print(f"🛑 {conta['nome']} FloodWait: {e.seconds}s (Esperando...)")
                await asyncio.sleep(e.seconds)
                
            except Exception as e:
                print(f"⚠️ Erro: {e}")
                await asyncio.sleep(0.1)

    except Exception as e:
        print(f"❌ Erro fatal {conta['nome']}: {e}")
    finally:
        if client.is_connected():
            await client.disconnect()

async def main():
    print(f"🔥 INICIANDO MODO TURBO ({len(CONTAS)} contas com relógios independentes)")
    
    tarefas = []
    for conta in CONTAS:
        tarefas.append(sniper_individual(conta))
    
    await asyncio.gather(*tarefas)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())