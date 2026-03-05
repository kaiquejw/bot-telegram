import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzsBu09YN8UXHROCrPdpl7c2Ud5vZD29RapK-RkZ-p5mjq3unMf_MsPeJ7a0Shx2eE-UmlOK1jdCYFJLJKYq0BJvlxOK3UV_Ta_ZNNJ0aoE3nhoDTRvICtrH5AWoNA0weNlsRhvIuaM-7yQt2kbe-d4P_qWwinTmp9p8D7GE3Y3XmchzUeczCmsQPtzZOU5yFgG3-JDbC_ojc9zyO5Hh1dpGF8Oq41uvWAdNo9YqJXAQ4m__CEwW7s1zQ-GBWkpnlMGLwqZ7VMHcgvNR-5e1o4PfgGgkveAQU3RGAlOc-niX_Z6toVgAXm3VdfeyCet89xhWfNIr1lf3WLgw2D9Glnf7-pE='

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