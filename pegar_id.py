import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu30eP1SJRHT5qu5zpJ3QY4NERMZsWae84yPej_EhYt9MMaB4c6K5bGoOWUfH4BikUUSXrvZfsrWPaFf_GPSYOrkyoSkIA2Dri2NkBen3FoPiKef1phr2hWiYq1nnKVr7OE0zrjR6QtBVGjJKeuProuL8OehkgwpSX3gyM-jS3XTusBbGJAmno4wcTehL2qrPuChqDJlz1CuwHoxqBStiE2Ct5kvIeWUBihNo-IRG1mbhqNLsbCbCB5Ed6EficW5V4w_9hk4WIRcj0sMr4s6AO69TjJkY--2EfFfzQCEp79rkwRfbl8T6Vv5QM8-0cBeLR3SFWt70t0u_gz_3C6wNNCU='

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