import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS OS DADOS AQUI ---
API_ID = 31891041  
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu5lDIZ7j88Pwb3ITqtfarMo4mT_G28NIDDKTNNaWvvU0zTEehN2F3nXgsNh6Vvl89UDdFpgDBjIw2brSJyWCVYBybL92pbIW9bh2HefPbxhrlhWBXg3oIncGJSkVkUKfhKktVYvC1o28T9Fes9D-o_gVtrWO_54QlKo8jhGW3c2auC0YjNLzBjiUsl6Fe-o1BVNJbL8erYz3IrAmtElOGeGPttibYjptk9_bpPNUfJEFtntN2k-MR8n_QHs4nzwUvMyPKHM5N8cF6IJbNzeynvGCkkEUQYRX1XVJQ7SKcjeyCNPIjj1B5CyLzlss1mEAizNMfvMxYBSBcxELWuGsGSg='

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