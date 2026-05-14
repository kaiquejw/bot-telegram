import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu8ULuIm-fVJTa4xZXREsQVitNeppDGkhYrovgHh-_zkVPNrgWr-NIoFOhQRmQBrDUnB8_o4lKnK_lhSbLoyWvi4aXuKxsk3i086-JDJSJOrNOFplAZQLmwoSLTCh4YaAYvj7rezhr4JpSpp0ZhDjwmk8dL4V1rK5V4tEAY3NtpHey6T8b9zE96HpZxsaaIe7JuFZ-24SZgl7FbTSMRQ7DTwmlo9DWz1BH5JcYPyCHD8lmTphP7YG6632qD6AzSB_6OIDquo3zSfUVLM1o42inTHInzfQVbleA56q4hFXjlWWnfhLPMWn72a0GQAHctrWclqJjwZ4gxrFGAN12tfOKVI='

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