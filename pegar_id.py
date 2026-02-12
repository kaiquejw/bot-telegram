import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuxrkYYPUDrGVXaVKDMzxhnsb-1m4m4LuSeFU5vHmTeXJlGukJCMVBJy1DEm7tZl7A91hF0tNQGzABWdy-BT3GzWjdHBnBKqtzzdX621p1w-esNLg_lYwXsU09lc_Mloj_9tDWJYXSXlmXx2rZYCxUpwmSqa89AlFM1VHlw56wGFRJqfhksCWPSvKKf7_aurRlvMKfpUXmtfefhRu0yo2RHAvU1Dj6H_g0FznD8UF_fwAuLd9V_YqQH-MF4eL_miZPTVIZaBS_ALzCivt5auwCkh1cauQ58wRsVDMGcdo2p4v4zZK3bp-G6gpTJQeOwlKPD5X3eodcnniZ-0NTuM7HwU='

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