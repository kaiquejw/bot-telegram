import asyncio
import os
import datetime
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.errors import ChatWriteForbiddenError, FloodWaitError

# --- CONFIGURAÇÕES VIA SECRETS ---
API_ID = int(os.environ.get('TELEGRAM_API_ID'))
API_HASH = os.environ.get('TELEGRAM_API_HASH')
SESSION_STRING = os.environ.get('TELEGRAM_SESSION')

# --- TRATAMENTO DO ID DO CHAT ---
raw_chat_id = os.environ.get('TELEGRAM_CHAT_ID')

try:
    CHAT_ALVO = int(raw_chat_id) # Tenta converter para número
except ValueError:
    CHAT_ALVO = raw_chat_id # Se der erro, usa como texto (username)
except TypeError:
    print("ERRO: O ID do chat não foi encontrado nas variáveis de ambiente!")
    CHAT_ALVO = 0 
# ------------------------------------------------

# ⚠️ AJUSTE AQUI PARA O DIA DA COMPETIÇÃO ⚠️
HORA_ALVO = 14  # Exemplo: 20 horas
MINUTO_ALVO = 21 # Exemplo: 30 minutos

async def sniper():
    # Conecta usando a sessão salva
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.connect()

    if not await client.is_user_authorized():
        print("❌ Erro de Login! A Session String pode estar inválida.")
        return # <--- CORRIGIDO (estava returnss)

    me = await client.get_me()
    print(f"✅ Logado como: {me.first_name} (@{me.username})")

    # Define o horário alvo para HOJE
    agora = datetime.datetime.now()
    alvo = agora.replace(hour=HORA_ALVO, minute=MINUTO_ALVO, second=0, microsecond=0)
    
    # Validação simples
    if alvo < agora:
         print("⚠️ O horário alvo já passou hoje. (Se for teste, ignore).")

    print(f"🎯 Alvo definido para: {alvo.strftime('%H:%M:%S')}")
    
    # --- FASE 1: ESPERA INTELIGENTE ---
    # Agora ele espera até faltarem apenas 5 SEGUNDOS
    while (alvo - datetime.datetime.now()).total_seconds() > 5:
        restante = int((alvo - datetime.datetime.now()).total_seconds())
        
        # Mostra aviso a cada 10s para não poluir, ou se faltar pouco tempo
        if restante % 10 == 0 or restante < 10:
            print(f"💤 Aguardando... Falta {restante}s")
        
        # Dorme pouco para ter precisão
        await asyncio.sleep(1)

    print("🚨 MODO ATAQUE ATIVADO! (Faltam < 5s) 🚨")

    # --- FASE 2: ATAQUE (Burst Mode) ---
    enviado = False
    tentativa = 0
    tempo_limite = alvo + datetime.timedelta(minutes=2) 

    # SUA MENSAGEM AQUI
    MENSAGEM = "Kaique [preso andre raio 5]"

    while not enviado and datetime.datetime.now() < tempo_limite:
        try:
            tentativa += 1
            await client.send_message(CHAT_ALVO, MENSAGEM)
            
            enviado = True
            print(f"🏆 SUCESSO! Mensagem enviada na tentativa {tentativa} às {datetime.datetime.now().strftime('%H:%M:%S.%f')}")
            
        except ChatWriteForbiddenError:
            # Grupo fechado.
            # print apenas para debug, não precisa poluir o log na hora H
            # print(f"🔒 Bloqueado. Tentando...") 
            await asyncio.sleep(0.25) # 4 tentativas por segundo (Ritmo seguro)
            
        except FloodWaitError as e:
            print(f"🛑 FloodWait de {e.seconds} segundos.")
            await asyncio.sleep(e.seconds)
            
        except Exception as e:
            print(f"⚠️ Erro: {e}")
            await asyncio.sleep(0.5)

    if not enviado:
        print("❌ Tempo esgotado.")

    await client.disconnect()

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(sniper())