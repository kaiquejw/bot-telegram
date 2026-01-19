import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu7LdHhkUgegD_UDAkuBpReEJYk4iMqy48e3-6PzicRg8vr_NrIkLy68t0-E9bqb4QWNWnqW4IyLhQ0586S-63EqxJRax7Z3ti1yMRGfX82QkXP_2MgogHItj_ZwKB29C7q3aAL-j25vP7VEZa72298FQX0_BQWM9jbEvF6Oomwz524WevRLzwkV8XVuJ11MkX1W4g2oSyLivpXI_I0XdX9jpUS23Rs3PUbOkWcmPNzDeecACV0UlOasVqLbRW1TmscyhvDofdVsfqFTP4rPWK2O8CjhKMCCx0SX0wfVhoKGqM1xtlmkf-Q9MpjDOxwAnGkL4F_hJaY4lSPWg6hWiHlE=' 

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