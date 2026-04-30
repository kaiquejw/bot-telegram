import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu3sjUEZydvwgPx3QEYZXSXOgYhAFGCm1mYIOoU_qemZI61n6Kov5yagoQJPxke-VrSp5wvlEjqe6fBDKAqk4I6tSpUNRRMPTv9f0d9iOaLqe2h1Gru5wGMgeeWa0PJYG7ChnPKcFqdIZ4hBQbwfHCKytYudv11BHvGJAl6FATyjCUkIAQGUFrCjtaiXTzuQTRZRPigRQP_Fu2Tb5Toa5MVSgE4konWHSSgGC1mNNLrsWfoxK9eYzzoLcIm3o8qIgtPyKzwG2cWSyhVbI0hbtSjQ5gkklovh_T6o69L9rnq2nRiICriVE11xLCO9JIUuObOWOy0YxodAWlMxNMUIGijM='

async def main():
    print("Conectando...")
    client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
    await client.connect()

    me = await client.get_me()
    print(f"Número de telefone da sessão: +{me.phone}")
    
    print("\n👇 AQUI ESTÃO SEUS ÚLTIMOS GRUPOS/CONVERSAS 👇\n")
    print(f"{'NOME DO GRUPO':<30} | {'ID PARA O GITHUB'}")
    print("-" * 50)
    
    # Pega as últimas 15 conversas
    async for dialog in client.iter_dialogs(limit=15):
        print(f"{dialog.name:<30} | {dialog.id}")
        
    print("\n👆 Copie o ID (número negativo) do grupo 'Teste' e coloque no GitHub.\n")

if __name__ == '__main__':
    asyncio.run(main())