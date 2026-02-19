import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzsBuzZ9upvbjq3oFkO3u8Yy0FilybqmkejwkDnLnSy_1SDIVtpyBNaxu_HzuKEi5576HpRy5F8GqXoffwWfdfcKa_BpuCyfiNWRqI4E0Bu0P_cCYiPRfoRS1CsRNtUKIfpJfUiDWEYCTIJQ6tGUIcybUWRBdcMxthDnMXxLAFKZHwOfBdpsMuTUMCmUWorqgXBoCIkBEZfqldNFk9nxlXYNtwDKHhx3CWOzAlduiijMJyNlldc4-iUMJsam4etxIAppECcgZFJp474TZ9pCy56EB2cvcH2MA9i4lP1wkgzpyIJNhwZ4Ln4kuZVHg0CPcPGH56xIUErR7b0lC_8cQzBcauw='

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