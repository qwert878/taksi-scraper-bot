import asyncio
from pyrogram.idle import idle
from pyrogram import Client
from pyrogram.types import Message
from app.config import API_ID, API_HASH, SESSION_STRING, TARGET_GROUP
from app.keywords import is_taxi_request
from app.config import API_ID, API_HASH, SESSION_STRING

print("API_ID:", API_ID)
print("API_HASH mavjud:", bool(API_HASH))
print("SESSION mavjud:", bool(SESSION_STRING))
app = Client(
    name="taksi_scraper",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
    workdir="/tmp"
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

    try:
        await app.start()
        print("✅ app.start() ishladi")

        me = await app.get_me()
        print(f"Kirdi: {me.id} | {me.first_name}")

        print("📡 Tayyor!")
        await idle()

    except Exception as e:
        print(f"❌ XATO: {type(e).__name__}: {e}")async def main():
    print("🚀 Bot ishga tushdi...")

    try:
        await app.start()
        print("START OK")

        me = await app.get_me()
        print(f"Kirdi: {me.id} | {me.first_name}")

        print("📡 Tayyor!")
        await idle()

    except Exception as e:
        print(f"❌ XATO: {type(e).__name__}: {e}")

if __name__ == "__main__":
    asyncio.run(main())
