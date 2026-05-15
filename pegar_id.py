import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuxC9uxn9wa0qtJP9XbwkKk3TZXarD0n1ajdala_h6Q9gGXIdMQf2tBFkIAtkYJfuGcxTTmVc1RYpTuKPAIBB9XMIpRHdgiJ-f0Ga3wKT8jTU3wbGffTqbw7xvhr5hozkENg_elaiFNEqfqtAznAWqM6-wtXc3soLW0A2wNvtirmORHP1NlDS1UJyNoBsUxIsliCC3XZin24Mkna9nJ4LpOQtBHC7zG0mMJN29DXByr1gJa34ZjjUT8xOWzYLVccZIOi-Wo2fny37PbRkxJA8dahJp8TZrLwP8bVn-GlezC3UDue-_Vk5LNiSDwoUlrDQ2I1kdXpWEAHBAdzm4oAmhY4='

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