import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzsBuzmCAoFcCke7PWiGADK2EbxWIkI3UOn-mwM7yPiEFpWFKMULuZEQfuFue6AvVFMJCaqoJzuCUaxdiP9mKfKFiB03F9zqAhHosRarbG0cJOgUws5xlMEk2LTHMR9iwvitzPIAO1Mq86JW_i347l8Ot5S3CKU77hJjI2yqEuHuJ-O0boMLeQIWtfGc745IHc0mnRynT4xyMHazfOQpMUHWL0rZdQR9FgL65AqJVxpEfVxQiK1yi8n4yCFSJbYFD_jnReFm-uKkIvu3JKM5BouQabKJfMJNUNYVGcpaNerktueaJUgZdZ9w93R0SYC05PpcSuNi4zByqTzpJInDEXzn7R4='

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