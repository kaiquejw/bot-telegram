import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu1KJwrAjESxu0IecZwMagQR3GWbbqs_KA6XCFBDJZUoGLXnTd7ixSYjhjxL4R6qcZICgbaVJMXlq-zxn_t7DEQkx5LJA-Sn_9l7DmZONn6p2OffN0gcrC53PUZWgoGFHy9Ze_W69_Vgs4mNIIpFn8xskllJido2RDfT10fIOzsmefSTF78psXBhZz56nriAfzttddi1JiFG7tSuibMLrkV2yoH3eJH8-lupWcEYOlzzPlbGE15nuyZT0rhjmjdcSZqhYeStYPqRNB2Mk7jg0abZ8axDOfjljgeYFVbrSijHnRnMmIyZAhKbbxEm8fgFmJfVU1YDjGobNyFqOrf8e9gs='

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