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
CHAT_ALVO = os.environ.get('TELEGRAM_CHAT_ID') # Pode ser o @username ou ID numérico (-100...)
try:
    CHAT_ALVO = int(raw_chat_id) # Tenta converter para número
except ValueError:
    CHAT_ALVO = raw_chat_id # Se não der (for @username), usa como texto

# Horário ALVO (Ajuste para o dia da competição)
HORA_ALVO = 12
MINUTO_ALVO = 50

async def sniper():
    # Conecta usando a sessão salva (sem pedir código)
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    await client.connect()

    if not await client.is_user_authorized():
        print("❌ Erro de Login! A Session String pode estar inválida.")
        returnss

    me = await client.get_me()
    print(f"✅ Logado como: {me.first_name} (@{me.username})")

    # Define o horário alvo
    agora = datetime.datetime.now()
    alvo = agora.replace(hour=HORA_ALVO, minute=MINUTO_ALVO, second=0, microsecond=0)
    
    # Validação simples de horário
    if alvo < agora:
         # Se já passou, assume que é para testar ou configura para amanhã (opcional)
         print("⚠️ O horário alvo já passou hoje. Verifique se o fuso está correto.")

    print(f"🎯 Alvo definido para: {alvo.strftime('%H:%M:%S')}")
    
    # --- FASE 1: ESPERA (Modo Econômico) ---
    while (alvo - datetime.datetime.now()).total_seconds() > 15:
        restante = int((alvo - datetime.datetime.now()).total_seconds())
        print(f"💤 Aguardando... Falta {restante}s")
        await asyncio.sleep(10)

    print("🚨 PREPARAR PARA O ATAQUE! (Faltam < 15s) 🚨")

    # --- FASE 2: ATAQUE (Burst Mode) ---
    enviado = False
    tentativa = 0
    tempo_limite = alvo + datetime.timedelta(minutes=2) # Tenta por 2 minutos max

    # Mensagem que garante a vaga
    MENSAGEM = "Kaique [preso fulano raio 1]"

    while not enviado and datetime.datetime.now() < tempo_limite:
        try:
            tentativa += 1
            # O parâmetro 'entity' aceita username (@grupo) ou ID
            await client.send_message(CHAT_ALVO, MENSAGEM)
            
            enviado = True
            print(f"🏆 SUCESSO! Mensagem enviada na tentativa {tentativa} às {datetime.datetime.now().strftime('%H:%M:%S.%f')}")
            
        except ChatWriteForbiddenError:
            # Erro clássico de grupo fechado
            print(f"🔒 ({datetime.datetime.now().strftime('%H:%M:%S')}) Grupo fechado. Retentando...")
            await asyncio.sleep(0.25) # Espera 0.25s (4 tentativas por segundo)
            
        except FloodWaitError as e:
            # O Telegram mandou parar
            print(f"🛑 Cuidado! FloodWait de {e.seconds} segundos.")
            await asyncio.sleep(e.seconds)
            
        except Exception as e:
            print(f"⚠️ Erro genérico: {e}")
            await asyncio.sleep(0.5)

    if not enviado:
        print("❌ Não foi possível enviar dentro do tempo limite.")

    await client.disconnect()

if __name__ == '__main__':
    # Loop de eventos do Python
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(sniper())