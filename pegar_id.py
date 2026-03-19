import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS OS DADOS AQUI ---
API_ID = 31891041  
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu5U0QDkGOJ_Pi8uFp9DqenfWOIegOZ8VsLUXtAP5p01azwnmBXiSsgkLIc-Il4O9AjHfK3oG2slOYIQhYlZ6rpnsjZxLMy2VkXWB4r0I97kptPCdnMTzLvU-GXyJojBRzSK26aI40R0ktAKoIHi9tb8OvJ31LuzsWZifhQ37F5KDB8syzeM-JsfebmkTiVKFGb2_U84DDs52D2ioBm93U9sNThfHbFcEZZrPX1tNghWeIo2hSe_LpiWcF9rJtdix5MKTLFiYF-9QRnAV3Hlt8fYPqqhUGpuONyAW0D15ApEn5f1_AjUCoA3d0m8ZUv5LGsX6LHFL1ArSI3ymTSxrMN4='

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