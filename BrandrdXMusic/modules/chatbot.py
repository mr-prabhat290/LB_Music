# BrandrdXMusic/modules/chatbot.py

import random
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import app
from config import OWNER_ID

# Simple random replies
REPLIES = [
    "Teri gf ko leke bhag jaunga 😎",
    "Kya be? Tere jaise 100 aaye aur gaye 💀",
    "Acha baccha samjha hai kya mujhe? 😈",
    "Emoji se darrta hai kya? 😂",
    "Bas kar bhai, ab rulaega kya 😭",
    "Tera logic NASA wale bhi na samjhe 😵",
    "Mujhe trigger mat kar, warna AI hoon bhai 🤖",
    "Tere jaisa chat main 10 handle karta hoon daily 😏",
    "Thoda respect dede, Innocent Aatma hoon 🧘",
    "Bhai tu serious hai ya joke kar rha? 🙄",
]

# Telegram sticker file_ids
STICKERS = [
    "CAACAgUAAxkBAAEEfS1lkg1OUxT3lW2HwO5muRIT3l74uwAC5QMAAqbCkFbY5js4NNTmVCkE",
    "CAACAgUAAxkBAAEEfS9lkg3t3Erzbo2WDx2TTZ1VwS5k-AACpAEAAkb7kFcph5pwKaxFGSkE",
    "CAACAgUAAxkBAAEEfS5lkg3ulN5Hmeog9jOf2cNohkOqOwACuQADVp29CkUmwTXUIGezKQQ",
]

# Memory context per group
GROUP_MEMORY = {}

@app.on_message(filters.group & ~filters.edited)
async def chatbot_group(client, message: Message):
    if message.from_user and message.from_user.id == OWNER_ID:
        return

    # Store last 20 messages
    chat_id = message.chat.id
    if chat_id not in GROUP_MEMORY:
        GROUP_MEMORY[chat_id] = []

    GROUP_MEMORY[chat_id].append(message.text or "")
    if len(GROUP_MEMORY[chat_id]) > 20:
        GROUP_MEMORY[chat_id].pop(0)

    # Randomly decide whether to reply
    if random.randint(1, 5) != 3:  # 20% chance to reply
        return

    # Select random reply
    reply_text = random.choice(REPLIES)

    # Sometimes send sticker instead
    if random.randint(1, 6) == 4:
        sticker = random.choice(STICKERS)
        await message.reply_sticker(sticker)
    else:
        await message.reply_text(reply_text)
