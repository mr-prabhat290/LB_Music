import random
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import app
from config import OWNER_ID
from pyrogram.enums import ChatType

# Memory for last 20 messages per chat
context_memory = {}

# Sample funny + gali responses
funny_responses = [
    "Teri GF ko leke bhag gaya 😎",
    "Bhai tu to full cartoon nikla 🤡",
    "Abe chup reh, bhauk mat! 🐶",
    "Tere jaise 4 dekhe hain maine 😂",
    "Tujhse na ho payega bhai 😏",
    "Tere liye toh CPU bhi sochta rahe 🤖",
    "Abe tu hai kaun? Google ka chacha? 😂",
    "Aunty ke phone se aaye ho kya? 📱",
    "Tera dimaag offline hai kya bhai? 🧠",
]

# Telegram stickers list (add more if you want)
stickers = [
    "CAACAgUAAx0CcRkshwACNWhlQ7P9bLfaMx9H8zvqNV9P0wACogMAArV6CVVsNJ4gDRzzazME",  # random sticker
    "CAACAgUAAx0CcRkshwACMWRlQ4WuRE60JGM7zBvczExjbAACewEAAmYugFYHhkS0uMQ3JzME",
]

@app.on_message(filters.group & filters.text & ~filters.bot)
async def chatbot_group(client, message: Message):
    if message.from_user and message.from_user.id == OWNER_ID:
        return  # Skip replying to self

    chat_id = message.chat.id
    msg_text = message.text

    # Save last 20 messages per group
    if chat_id not in context_memory:
        context_memory[chat_id] = []
    context_memory[chat_id].append(msg_text)
    if len(context_memory[chat_id]) > 20:
        context_memory[chat_id].pop(0)

    # Only reply randomly (e.g., 1 out of 7 messages)
    if random.randint(1, 7) != 3:
        return

    # Build fake context from memory
    fake_context = "\n".join(context_memory[chat_id][-10:])
    selected_response = random.choice(funny_responses)

    # 20% chance to send a sticker instead of text
    if random.randint(1, 5) == 2:
        sticker_id = random.choice(stickers)
        return await message.reply_sticker(sticker=sticker_id)

    # Else reply normally
    await message.reply_text(selected_response)
