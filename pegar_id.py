import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzsBu71J3CxyxtLpzdFj0t27JbUww0trWqgaUCBliWl-EcuyF3JYmcBCiQjNk05Tj4bkEGtHQrtnPC0271nD9rags4u9XVRObhWdW-btZeF9KFFRpIA9TGc5xu-kNPDyIboubtjfhEvrRMmZCeA1Y2ZDt4V1MMD2hhJ6KCCp5rq0QojaDcr4fE_ayqeKppcLDuDcARL2iM8vlNM2p_XBqbYeXgiqcp2P8S99D6ubmqYLBMt3lepW7RxRYchYjG6IXF2WnsAoX67zjCRcp1INdN2HigawIQgiNXTI1J4F-FhwmFEsOftnzb7AGw6pfi2jzK4QFKuECRCiuV5TIG8ObATCmLw='

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