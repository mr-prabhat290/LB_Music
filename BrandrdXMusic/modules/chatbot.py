import random
import time
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import app

# Funny and witty chatbot replies
REPLIES = [
    "Teri GF mere sath hai 🤭",
    "Main AI hoon, lekin emotions tere se zyada samajhta hoon 😌",
    "Pehle khud sudhar, fir mujhse baat kar 😎",
    "Main tere jaisa 100 bana chuka hoon 🤖",
    "Aise mat dekh, pyaar ho jaayega 😏",
    "Tere sawaal se zyada mera jawab intelligent hai 😂",
    "Mujhe tag mat kar, nahi to tere chats leak kar dunga 📤"
]

# Music commands and other bot commands to ignore
IGNORE_COMMANDS = [
    "/play", "/pause", "/resume", "/skip", "/stop", "/end",
    "/vplay", "/shuffle", "/loop", "/update"
]

@app.on_message(filters.group & ~filters.edited)
async def chatbot_handler(client, message: Message):
    # Ignore music and update commands
    if message.text and message.text.lower().startswith(tuple(IGNORE_COMMANDS)):
        return

    # Reply to user if they reply to the bot
    if message.reply_to_message and message.reply_to_message.from_user and message.reply_to_message.from_user.id == app.me.id:
        await message.reply_text(random.choice(REPLIES))

    # Random replies to normal chat (not commands)
    elif message.text and not message.text.startswith("/"):
        if random.randint(1, 5) == 3:  # 20% chance
            await message.reply_text(random.choice(REPLIES))
