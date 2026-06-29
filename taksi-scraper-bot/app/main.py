import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from app.config import API_ID, API_HASH, SESSION_STRING, SOURCE_GROUPS, TARGET_GROUP
from app.keywords import is_taxi_request
# Session string bilan ishlaymiz (Railway uchun qulay)
app = Client(
    name="taksi_scraper",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)

@app.on_message(filters.chat(SOURCE_GROUPS))
async def handle_message(client: Client, message: Message):
    text = message.text or message.caption or ""
    
    if not is_taxi_request(text):
        return

    try:
        # Xabarni nusxa ko'chirib yuborish (forward emas, copy)
        await message.copy(TARGET_GROUP)
        print(f"✅ Yuborildi: {text[:50]}...")
    except Exception as e:
        print(f"❌ Xato: {e}")

async def main():
    print("🚀 Bot ishga tushdi...")
    print(f"📡 {len(SOURCE_GROUPS)} ta guruh tinglanyapti")
    await app.start()
    await asyncio.Event().wait()  # To'xtatmasdan ishlaydi

if __name__ == "__main__":
    asyncio.run(main())
