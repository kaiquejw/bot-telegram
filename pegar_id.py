import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzsBu3R7Upxiuoio-9PbynJVXDYJB7Pq_voeo5BogwPrHacXYon7LvPycOdLrAeb3WtoodG129TcVA-1fOOD_TBaTfa-tUvmtbiilKXFW3QsuLhmYAiJHnL1HDLoWTcmlfv1iZYWLIXzBuG8TNpN4u5_dsjxYKawwO3P8eTEjHYP9lUF6LU8w47kbpnmwIjyyDLsBJ3b238tUTUd1MPu4ZVrKQVLaAn0HrCbFXWc-Vr0upzgrYdhz8gr-LeuQjwgqQVCdp13wPgTI6ecHpIk3JPhU063NULAwqlD14o4gbjk8X9tQIC8ZHV0oGFWtiPze6wq-pUUQkPXba0rDZMPZyzT5BQ='

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