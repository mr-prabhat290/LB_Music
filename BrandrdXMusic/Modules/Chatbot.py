import random
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import app

REPLIES = [
    "Main tere jaise kai bana chuka hoon 🤖",
    "Teri GF mere sath hai 😏",
    "Mujhe chheda toh code leak kar dunga 😈",
    "Bhai zyada mat udh 😎",
    "Main AI hoon, tu human bhi mushkil se lagta hai 😌"
]

@app.on_message(filters.group & filters.text)
async def chatbot_handler(client, message: Message):
    if not message.text:
        return

    # ✅ Step 1: Agar command hai (/play /pause etc.) → skip
    if message.text.startswith("/"):
        return

    # ✅ Step 2: Agar bot ke message ka reply hai → reply karo
    if message.reply_to_message and message.reply_to_message.from_user and message.reply_to_message.from_user.id == app.me.id:
        await message.reply_text(random.choice(REPLIES))
        return

    # ✅ Step 3: Random reply (20% chance)
    if random.randint(1, 5) == 3:
        await message.reply_text(random.choice(REPLIES))
