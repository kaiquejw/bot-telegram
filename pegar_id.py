import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzsBu6DHJ0XxHG9lqdH5i17HoGUQgvDRoWdNW_0iQXXF-TA-zIKN2XxFF4OFu_6FXcTMf6pEpX8Mq2MF26FqFr7cd7Gk_qWIsmToh2C-C5u__ru8zEawH-zs-qthgwejGYbTXL3O2pdpCVZqENrRpJd_DLBcks6BR9DWGpYEPtBppglzgQ4HXYG0bpbyWp_BzeVgTTLH0O2D6ZayBmvkrHHf3sGnqt5EPNQ_Ix75QeHwyz_pUI46G15jhBi6NNevSpYnhGYh7rSkR439WXlUic-SirbkEg1aErOR7kMvai0qMODcjkiGHZs-yBMT8nz6cH1oRK0jn9Z5zoZSrqnqD7o-oY0='

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