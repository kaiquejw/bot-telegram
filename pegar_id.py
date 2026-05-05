import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuxpVqx5MzcJNAzRol09Q-jjwtAUY_4TRgDeJo0CFlLj538r9UzFSgQQ9YsZsQKrt3crgEaux-8q2DneyAu4AvctOwfSYmVXf-TrWSHgRouRl6-DI1_kPKjK5OMd-CwQf1b1op5yykc6Vn5EX-4eQ9KfZB77ecefiP9HcBzlawFsJ_9Je0B3jkZaeZTmDdkY0o3UlNBNZn3rEXc7zKvpN_x2hFdLhX4zE7Fo1lmV_BLyKX9g2lJEVA-E2sM6KrZIkoXZCTk5mql5WB7-129tsGjk0MyZebVNv3atEWihYSGwRjO2W2H7jqCzbDXPSUn7-rzT5CSHocqaGm0am6OLUVtI='

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