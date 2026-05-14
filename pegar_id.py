import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu6Sty7PTngGY0UhdcNWVrN4GYZAMwTZzpOyP-OqO4_zPlNm2vkFInAJLNf7qgPYn2RrNb7BjSaS-4Xtd2pFVY-c8Co5kidKm8Ry0WsQ3oh1Ps8zVklkZPctMHhVMAA767viCcgKXGvv5iN-RU5YCN16j6TDeMNI4p3xnTkNGxM4CK-SKfkZOj1zkF9z0pbPDe0X23QntejwEsu7kXsSMzFmfb6RzhBoBkWNsXdZ0DxvWdxZsn6aIvvwve0S4AuYk9Cfpbs8bbEysO2yEkE1SPAl2pUnq9opDiOm-wDnIRYnxl8DcLN7O2y9a9LmpLrl1W0UVCffIIlK3CECUCmhdoLo='

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