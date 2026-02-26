import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzsBu5mVQ_lZFGo05frG5CPFxXzWfaFE0eVMGAh4EVHd-U0miOtHJbbbaKvbo8Ax5h56-FnmUutgnqNBerBeVJ_0PRUEStFlMKQozQzeb6YQSna6eu3ZPlGjxKkzu3YHm7C3rTthL9BG7OPi1jKwjlw0z6NG2xaFBuYDT4mOjUn60t5yT1sk6gQpI8YfZzwRdOoqTTarC4-1lZ52uVP-h_5Or02f99hpsGRHvoQYp5CVgFAu0TpPqEetoBhscdAB1I_h680CYI4oEHDAvAJ4TKdEFpa10w362IGGtUZBdpkQPwJomdE_zP2A3F0SnCBJox1Vx-swAldhY8QT3GEu3HkwPYU='

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