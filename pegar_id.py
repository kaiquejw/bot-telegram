import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu4mNzdQCPHOauS6r8k6j15okDnV2obwPfQz2CR_wTKobQWLCOHakYc4PV-8qmPhbofZW7ai4NXWVdZSkkwSFVYMGwjZl96ukxDedhmwEFbQxrYDTcVW6yOJ070Ibi8nVgm0ydqD7LSlvUrEgi_BA7INwL_LBsz9hxIKwwNM8AskivJ7qAFwBl0VE-KTOjJJFYotMjOlbYuCm7WK17P0AesUHSVLKDjcBr4Vfn3UHiELX7ty-j8w2XbxXoKAEqCWfQdD2-nH3V_izoCAOySb7xOUKd8xPPZBYWOLRFKqejuv2qQIOV1oT2d-oDCxzSr2vg2mymLbNN79g0bAn0mxHrzs='

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