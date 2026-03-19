import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzwBu5etJUg6UccQDh_Tau4gef3qnvkH_KSKC7JFsRFBIN_MDrIxLtIz6XeG5TiX2x6VF64JhW7p3KkB62S9O77Jk_5GgVQufYrk-bF87R74G0BciGMv-HObA_1l0i471vtWSp0aKIaF0Li-vfKGMGqlqRYN9qDTQQvIe7AqGbDLXNUrnyeME73ffpdJ6aAq-eK-deRlpbqQzpoP1T_zeTQq1dvOcX-iPpdnixYvCEbz6ZMExd4J4rLLwaiPE3CQE4VPFzXDSxzYM3YKrFlW4FPv8HZbtvVNNMvVhvtwqlt1tnS7nBXXGdsJkggAYjdJD0JmndSg2N_9V2DWHfGfi7H5GnY='

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