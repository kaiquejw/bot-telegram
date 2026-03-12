import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzsBu1Tv-mR8IfTevbMDiVLV9fDLrIVoaBj_zuGs-PThkBmtfUftNlu3cS9sCJicaVKDMfHudnY9uycR2AmlxJA-aF1JZSdY8zQHlPbc7DeGyzkuJ9DruQSU2kL90vBJsAFAl1Yi_hteT8YPEoWkJcNLZ8GusUAdqMwY-mfqyO1ry6eUhv5lUAb31qTyRPuBZ2k2Hz0qyEyL0i-rPj68gYM_ck7L9rNDxugo2xYGK4WFjML2iMMhwCFQ3DKHXhN2jsK5yJqaa0evocI4i8wB7wrubLQgdsn8E2nR6n8tUVDACQb1OBaivLDNGndbO1dzjk_8XPV6d2Lw-3VUe87E2zi8za8='

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