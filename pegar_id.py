import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu5U1YHzzE4kN_ickuBFndzCIZF3gJ1FmnijlA3mCgOWSQmeii0ES606OQVoAmSJVBCnn5rmuOg90rqpLMQPHC01svcgC6fpjmDbTejuvitNmeAatnUSFfKfzEQsK-3oVUQJZLRagzVjv6kOKTG-srilReFqA_hlWq3St9u9vFjF6VblXqNubF-EGc6Z32pWLsxUoSbQqHkcUf0-ve10HTd_L6Qt7jgloqACfCMj6MdalMq01ooGbx6GREVONYEvJOblPvIbAEQfecX8r0q3WdOM4GKLHYixozdL89JtObTzmJLggmpslvXFo6sNgXSMM0loO8IWqT2A9IKoElMM9inc='

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