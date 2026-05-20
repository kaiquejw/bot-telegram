import asyncio
import os
import datetime
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.errors import ChatWriteForbiddenError, FloodWaitError
from dotenv import load_dotenv

# Carrega os segredos de dentro da Vultr (.env)
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
        "hora": 00,   
        "minuto": 20  
    },  
    {
        "nome": "Laysa", 
        "secret_name": "SESSION_LAYSA",
        "chat_id": -4999405862,
        "msg": "Laysa x Mg R5",
        "hora": 00,
        "minuto": 20
    },  
    {
        "nome": "Katia", 
        "secret_name": "SESSION_KATIA",
        "chat_id": -5296287589,
        "msg": "Katia pantanal r2 laudo",
        "hora": 00,   
        "minuto": 20
    }
]

async def sniper_individual(conta):
    """Função otimizada para VELOCIDADE MÁXIMA (Modo Turbo)"""
    
    session_str = os.environ.get(conta['secret_name'])
    if not session_str:
        print(f"⚠️ Pulei {conta['nome']}: Segredo não encontrado na Vultr.")
        return

    client = TelegramClient(StringSession(session_str), API_ID, API_HASH)
    
    # 1. Warm-up (Conexão prévia)
    # Isso garante que a conexão esteja pronta antes do horário
    await client.connect()
    await client.get_dialogs()
    
    chat_alvo_especifico = conta.get('chat_id')
    agora = datetime.datetime.now()
    alvo = agora.replace(hour=conta['hora'], minute=conta['minuto'], second=0, microsecond=0)

    if (alvo - agora).total_seconds() < -120:
        alvo += datetime.timedelta(days=1)

    print(f"✅ {conta['nome']} pronto. Alvo travado para: {alvo.strftime('%H:%M:%S')}")

    # 2. Espera inteligente de altíssima precisão
    # Checa o relógio 100x por segundo nos momentos finais
    while (alvo - datetime.datetime.now()).total_seconds() > 0.1:
        await asyncio.sleep(0.01) 

    # 3. ZONA DE GUERRA
    enviado = False
    tentativa = 0
    
    while not enviado:
        agora = datetime.datetime.now()
        diferenca = (alvo - agora).total_seconds()

        if diferenca < -120: 
            print(f"❌ {conta['nome']} Desistindo (Tempo esgotado).")
            break

        try:
            await client.send_message(chat_alvo_especifico, conta['msg'])
            enviado = True
            print(f"🏆 {conta['nome']} -> ENVIOU! TENTATIVA {tentativa} ({datetime.datetime.now().strftime('%H:%M:%S.%f')})")
            break # Trava absoluta
            
        except ChatWriteForbiddenError:
            tentativa += 1
            await asyncio.sleep(0.040) # Freio de 40ms
            
        except FloodWaitError as e:
            print(f"🛑 {conta['nome']} FloodWait: {e.seconds}s (Esperando...)")
            await asyncio.sleep(e.seconds)
            
        except Exception as e:
            print(f"⚠️ Erro no tiro de {conta['nome']}: {e}")
            await asyncio.sleep(0.1)

    # 4. Finalização e desconexão
    if client.is_connected():
        await client.disconnect()

async def main():
    print(f"🔥 INICIANDO MODO TURBO ({len(CONTAS)} contas independentes)")
    
    # Executa todas as tarefas de forma totalmente paralela
    await asyncio.gather(*(sniper_individual(conta) for conta in CONTAS))

    # --- O MODO SONECA INFINITO ---
    print("\n✅ Todas as missões concluídas! Entrando em hibernação...")
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())