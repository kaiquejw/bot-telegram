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
    chat_alvo_especifico = conta.get('chat_id')

    # Calcula o alvo específico desta conta para hoje
    agora = datetime.datetime.now()
    alvo = agora.replace(hour=conta['hora'], minute=conta['minuto'], second=0, microsecond=0)

    # Se a hora alvo já passou hoje (janela de 2 min), ajusta para atirar amanhã
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
            restante = int((alvo - datetime.datetime.now()).total_seconds())
            if restante % 60 == 0: # Avisa a cada 1 minuto para não floodar o log
                print(f"💤 {conta['nome']} aguardando... Falta {restante}s")
            await asyncio.sleep(1)

        print(f"⚠️ {conta['nome']} entrou em ALERTA MÁXIMO (Faltam < 30s)")

        # --- FASE 2: AQUECIMENTO E DISPARO ---
        enviado = False
        tentativa = 0
        
        while not enviado:
            agora = datetime.datetime.now()
            diferenca = (alvo - agora).total_seconds()

            if diferenca < -120: 
                print(f"❌ {conta['nome']} Desistindo (Tempo esgotado da janela de 2 min).")
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
                
                # 🛑 TRAVA DE SEGURANÇA: Quebra o loop de tiro imediatamente após o sucesso
                break 
                
            except ChatWriteForbiddenError:
                tentativa += 1
                # FREIO DE 40ms: Ideal para servidores em Miami (evita FloodWait)
                await asyncio.sleep(0.040) 
                
            except FloodWaitError as e:
                print(f"🛑 {conta['nome']} FloodWait: {e.seconds}s (Esperando a punição acabar...)")
                await asyncio.sleep(e.seconds)
                
            except Exception as e:
                print(f"⚠️ Erro inesperado no tiro de {conta['nome']}: {e}")
                await asyncio.sleep(0.1)

    except Exception as e:
        print(f"❌ Erro fatal na conta {conta['nome']}: {e}")
    finally:
        if client.is_connected():
            await client.disconnect()

async def main():
    print(f"🔥 INICIANDO MODO TURBO ({len(CONTAS)} contas com relógios independentes)")
    
    tarefas = []
    for conta in CONTAS:
        tarefas.append(sniper_individual(conta))
    
    # Inicia todas as contas ao mesmo tempo
    await asyncio.gather(*tarefas)

    # --- O MODO SONECA INFINITO (FREIO DO PM2) ---
    print("\n✅ Todas as missões do dia foram concluídas! Entrando em hibernação...")
    while True:
        await asyncio.sleep(3600) # Fica dormindo repetidamente de 1 em 1 hora, segurando o PM2

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())