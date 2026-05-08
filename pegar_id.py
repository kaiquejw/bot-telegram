import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu1rBcGg1lHRezUxDxW5gd99Xd-yFAyNysU8BbMVO2_-fbXotI9653Rvei1-YSlsZT0C94rfzUby8zBRaqM57igma4iRQAP6oCbtk4eDSvresVngpIrIZxau7nvegC5yix2wnwJUgOHqjeDhTCVFeWYjQ-CxQO_tTIorcnUYCmuGkodipQPcd3dUxD0I7hdL8Sb-XHg9mfu31oCTu4jR5Y4RxawDFJRoHlAuowWylonkLZ0DZ0gyce2uRk1oQlN5xcG8ymBjjR3T2eM9kVXDHjUOokJKZL7ecEtupF3GPkJ4A0rDTLMcV6b4Fdt_rIlb52jhMNL5VUii0uWHvnZeB6Pk='

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