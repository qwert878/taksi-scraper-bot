"""
Bu faylni LOCAL kompyuterda bir marta ishlatish kerak.
Session string olish uchun.
Railway ga yuklamang!
"""
from pyrogram import Client
import asyncio

API_ID = input("API_ID: ").strip()
API_HASH = input("API_HASH: ").strip()

async def main():
    async with Client(
        name="temp_session",
        api_id=int(API_ID),
        api_hash=API_HASH,
        in_memory=True,
    ) as app:
        session = await app.export_session_string()
        print("\n✅ SESSION_STRING:")
        print(session)
        print("\nBu stringni Railway environment variable ga qo'ying!")

asyncio.run(main())
