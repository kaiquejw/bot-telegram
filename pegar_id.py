import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS OS DADOS AQUI ---
API_ID = 31891041  
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzwBu5JGKkMhVxYBl-CAmfqWDfFm1C030W4T9X6ahio0RBaDnhVz2xv529dEiY6oE4tg3BLz60NwZixK6-6NQm34XeUKWBtwY6j2GnXFysEHIZj-EwlDpGEJ1fn07nrYdVsZCwSe2f9Lpb7tluGqJUQjssCt4UbUBYRusY5MqMX47PH2e4hNK7qul0ipUB8c9RiXYx6qd6B3zZ6Blq-0YNizwFoodedwIJbQr1jXlEBORLOHVtpeEfn452fe9AKhPmBflq-cudiPYK0IU3ACpZytlWHlcyS0D9vYMxcarmzjT2A9Mv8C7jiUay03IR8JSHjIRZ5aAGi2JIHXrhm58mpbm-I='

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