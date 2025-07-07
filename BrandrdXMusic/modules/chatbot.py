import random
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import app

# Masti bhare chatbot replies 😈
REPLIES = [
    "Aye bhai, chill 😎",
    "Teri GF mere pass hai 😏",
    "Main zyada smart hoon, maan le 😂",
    "Kya bakwaas kar raha hai tu 🤣",
    "Apun AI hoon, emotions samajhta hoon 😌",
    "Tere jaise 100 aaye aur gaye 🤖",
    "Mujhe chheda toh Google bhi confuse ho jayega 😈"
]

# Yeh commands chatbot ignore karega (music commands ya others)
IGNORE_PREFIXES = ["/", "!", "."]

@app.on_message(filters.group)
async def chatbot_handler(client, message: Message):
    if not message.text:
        return

    # 1. Music or other command ignore
    if message.text.startswith(tuple(IGNORE_PREFIXES)):
        return

    # 2. If someone replies to bot's message, respond
    if message.reply_to_message and message.reply_to_message.from_user and message.reply_to_message.from_user.id == app.me.id:
        await message.reply_text(random.choice(REPLIES))
        return

    # 3. Random replies sometimes
    if random.randint(1, 5) == 3:
        await message.reply_text(random.choice(REPLIES))
