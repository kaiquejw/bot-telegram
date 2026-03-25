import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu78E8BpamHMBHs_yEbW1217b76yyfQp0xkCSJJEYMswC29zKliWJYp4vfV-IXS37jEzn1F3jA85GTDI6SYYP1Dl-zemi6j8k2yWvJAFQ2GLeFtbxsrIKW8B9LVbEElU4vh0HBrIoFPTb1Wtp51nY66qfcgi-juED0updPb8xo3TooLJR6vl9Q75GD6bL8XJfh-vCtkxnjA_IOeNp5U_XtJeE1JaX6S9U44k2S_JvHwFHf7q6_yFZ-Bx39WJL7g-ofIovH013wTj222O832ZOMkjOvwXBiptg-Yy3pogMOq9E5gbahnQrbSiKF3sDg0sBSFadVXaMTRZU5ZPg2i2wecs='

async def main():
    print("Conectando...")
    client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
    await client.connect()
    
    print("\n👇 AQUI ESTÃO SEUS ÚLTIMOS GRUPOS/CONVERSAS 👇\n")
    print(f"{'NOME DO GRUPO':<30} | {'ID PARA O GITHUB'}")
    print("-" * 50)
    
    # Pega as últimas 15 conversas
    async for dialog in client.iter_dialogs(limit=15):
        print(f"{dialog.name:<30} | {dialog.id}")
        
    print("\n👆 Copie o ID (número negativo) do grupo 'Teste' e coloque no GitHub.\n")

if __name__ == '__main__':
    asyncio.run(main())