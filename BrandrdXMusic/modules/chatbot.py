import random
import time
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import app

# Some sample funny + intelligent replies
REPLIES = [
    "Teri soch se bhi tez hoon 😎",
    "Pehle khud seekh le, phir mujhse sawaal kar 🤨",
    "Tere jaise kai aaye aur chale gaye 😂",
    "Thoda pyaar se baat kar na ❤️",
    "Mujhe mat chhed, warna tera Google bhi confuse ho jayega 🤖",
    "Areey bhai, chill maar 😌",
    "Teri GF ko leke bhaag jaunga 🏃‍♂️💨"
]

# Reply to group messages occasionally or on reply
@app.on_message(filters.group & ~filters.edited)
async def chat_bot(client, message: Message):
    if message.reply_to_message and message.reply_to_message.from_user and message.reply_to_message.from_user.id == app.me.id:
        await message.reply_text(random.choice(REPLIES))
    elif random.randint(1, 5) == 3:  # 1 out of 5 chance to reply randomly
        await message.reply_text(random.choice(REPLIES))
