import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu2TgZY2FHtyUzY9LdnANh4OYVVHlcKxrV6K5TdlmXfPB3gNaTPv3sVi328PYUCncl5gqGRP4W7hLo-p62_z6g4G5MiAQdySGsBw6QjB9JU4OdkxbiyUVllOKaxljSUwQyTnuC29vf7e_fEhGImOF04HwC-wx6g_qq5-CBDM_K5nhi5vnKkgMHR_PcQo3XbsnNKc2vdV-Dwp2bDXcVCWy6N4_wbCRP0RBldCGpVB-mED_Lww-qpH6NGV9B4mJWXR60zp167OFDMBGt2HynZGA0urpAcmKesavHyYmAVUlPxLSwk5_5VduT1jXH_dk6dfZcVSnKa4mj1Lga0tud2neky8='

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