import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu6HYkNLAr-BL5oJu9eCei8c6WzPmIBmb6kW6SW5K6z2IW9Umv-qXR9wyj7N8f6MnpoEDGPFtSKjyLq9s36j_eO2j44qw95GoY5rLgJCOgU_F2kt9K7J_b1qA_waukaqHoZXo1KamTRWZJGz5ICLBiFWPmmtRlBADqsUyUeMPE6uwZNeN17OXe6n4ze8FzuyjPxbXVBdlp-k_mUu32tUPY86-U46qW4N3VhHs3LJIgJu891EcDF-2LHdbLcElcc2bdj01CsBJLTcYDzqE9LwknVv-L8cAkG6zX1iHVOwzZNXZs_tkBtkBDbtxWjzfqvo6ohgiboz83qhEUU8-TITu_xg='

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