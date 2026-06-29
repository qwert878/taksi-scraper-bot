import asyncio
from pyrogram import Client
from pyrogram.types import Message
from app.config import API_ID, API_HASH, SESSION_STRING, TARGET_GROUP
from app.keywords import is_taxi_request

app = Client(
    name="taksi_scraper",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)

@app.on_message()
async def handle_message(client: Client, message: Message):
    text = message.text or message.caption or ""
    print(f"⚡ [{message.chat.id}] {message.chat.title}: {text[:50]}")
    
    if not is_taxi_request(text):
        return

    try:
        await message.copy(TARGET_GROUP)
        print(f"✅ Yuborildi!")
    except Exception as e:
        print(f"❌ Xato: {e}")

async def main():
    print("🚀 Bot ishga tushdi...")
    await app.start()
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
