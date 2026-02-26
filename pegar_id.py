import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzsBu1O_enprkygobmXr1aE5gMC1unv8yvl22Wt0vh1ihSObmj6ZMaeJi2bvzyoHqDcJAjBodSkgiIt5UXYbL5rUR-_jwgRwo8mZRTmcGHiT11gKKI0e5tjFTyKxQbMkY8enwVp5SrlPse0YKVe4WfsKUDEzE-V10mK3MA6B1zGBqmWmCX1Xyopha23nN18_aQKn7JwFIruhQKXSotET-n6CCSP82jVPMGMSUkhCUIrccaFqcb4P-0W9jI1RAOTD74MfjmcITlTVas5WKvIx2ZcJa5jaW_EaMRfDb9WAh2hQknkiXUv1KxIqZeU-In6dn9jfldSEeXbaLUwtr8crNxHJyb0='

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