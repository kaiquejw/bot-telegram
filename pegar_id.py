import asyncio

from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 36016816  # Seu API ID
API_HASH = "9045f8b49a3f8d0a44163d584c2b133a"
SESSION = "1AZWarzcBuwt4gVT-Wxd2lWea2cSF6kTmolpwfxwoL7A9AptnPzhB6UUVwo4vXCTmeOcEWTBfsxpJM5ABp0w95tUJW4fvPjeaHEVATecdx-yV_yYrA9U8lbMc5P0n5Xuphvxw5p5gZT0Yj9Y0qzs6GJVaIdgUb4zco77LNMyygPMSTleJyokM_Y_edIOBopZgERi_WZh6D6TilhHDJwmQto8ybTnVvoZqbZBQivqv3dBe9JcNMfGtg1An9suHXAPuwA_KO1-dmDseRlzYkbxQw2jXIt9BSlHrkBECT-Pd50btqQGxExLoiFwe2cKXGWk0YSe2su6OlTpk4mXW1Q94xJ8Jd_2v7TQ="


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


if __name__ == "__main__":
    asyncio.run(main())
