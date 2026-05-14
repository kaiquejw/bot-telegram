import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu5u7MIO0UqAi3hmhjcCObxCeRd2EzcXFHMxIpOjhcfKbWWhV_aZUwicIHo_mwi8ZpYyssKZMqECL9e2579yZF-sQTH2P4eE-TP9ht_-QHpVIpihlvQUVaetfhSRatxvkFQZH1buDn1HyzvUlyS4ewROcw1aqrIdpWnGSWYANtfePP_NpgXBr5swa_5EiX6lno1IwGirbUnTmwFjNjTNvPskTDDAgcqYL_RYi14SZPqCzhqgVp9wBWBc-OzWLHkNs8YvOgdyAq5rSoTuX9ODbi_A5fj5mfT_2d4622YQSCVU97PAaav3MEUVm2mOl4tJkiFg5DWB1cIZnxM__Qpz-Rik='

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