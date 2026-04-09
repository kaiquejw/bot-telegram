import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBux9Bcwub94zCVqkAv6Ogc5-C3WeEBxB2lB4IiCRLW8SU0VV0BVoBrnw4QPHbWAHzEpEjDbMIfh7PJ5Xifsw37HLS5Tm3x8RgaErRC84IRzlzwUkeJ2Bq2qrC0NFGe_noc8doeKwCEv_sKMda2NvImM3O63xaNXUt84nazyLjfvgwMnOWLcNka3GGso9d6qDF-fSR_GORurqzdi3aiHcZcD00EsRTmr-ffkLr9jh-ELbt7EV-W7GAiJnuuByXIa6uYKTFbckJQPJePSfRKBNzjs2p9LukONYiJqY5VjmZ0irbZ48oXtvdwpm6ktFV8UizbWuY1-YU4fvazMmQs_6L0w4='

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