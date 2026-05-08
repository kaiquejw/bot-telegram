import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu04TH81_GbhYEXax6fXuXheeYE7uAk-hUS1Ez_EJHnfRAGe5nZNsZJ2uoDR-bNz3p4_j-yushVpnBiMoLLh021uT5oOsZzIV4t9_dkgWRaW9TDtntigAJltCkMQdx7Mw7-3yLbGQOmUnWLvbEuubGC9CHw-cVSlxqA_FlF26tGwYl1pimjWgCdCMsdKgASrRBSgWbCFzZ7nm13WW7cIPrgzQ5_lrpYGiZkl_j13-kVS8EMYwy8wWVMDqa66q65_TTrNR5FVOP6H2-P3Lyc05qBFxlfeE-7VmFFDKx9iIHq4wWX9W8pxF1_cK4GNCi60Vy4CyaDpTPeEaStpOo1B13D8='

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