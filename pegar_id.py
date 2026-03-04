import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzsBu3Yp1I_8r6frS9djrAfHUel-Rsr_2SNqokvtU5Zb0pb79gh357XCFXfaAnDvgJt2ZlvpvbKKIIkiNM_t0QBk8lZImIj8oBf1qO0Lo93ipXcOHBFNLdsvmBsRJt3Aux02Hm3dyAdFesdXj3Sy_KUmvIDx0kFBRF20AjwIxs9U-BiSwh2vixcgiugwEGHkW_29m7OytfemqAdnwZ28SIvLSMfQob2GdvpvjF60DB5uDZLYOJHtUxUmQsziYdbvNEmMGGXuTB7lcPu5sopF6sp0Pma10-ql4mWLjHgG-VaG5GmO-nx3_OV0YGy1HiNQx8JzQadnQNtGsl7DjYX7M7S2nfc='

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