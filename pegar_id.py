import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzsBuyYUMqfsNcmBG-Zv4TIHiXYAVrfgAY9eyTmx40WJ1APiUxw_qbPRBCDkaJKThGozBwTPWec_yGDpSWzj32t0d8Y1tZ8iGefQJN1GQs-XNDIjNKqU7WrjiRPpTDN0C-39CEtzCdn1L0UZx_Z582_IORypOGl-DWgpkh9PApVnN1DQpMV0opKh1EGkv2WJ6pFE9QOjaU4SUVISpxnmLXsTiTM1jigQylvW_6r2oW4HxAvLCGli_mVTgvnpe21Ztbx8KB54rqIey8r34ndP036Qx2lT4ed7cgODsKwu4Jr0Ve_aEb4VXbuDNjOa6XDPYbe1xooZRGMYSaS3jdOwALrN3nk='

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