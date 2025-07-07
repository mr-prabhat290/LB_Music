import random
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import app

REPLIES = [
    "Main AI hoon, lekin emotions tere se zyada samajhta hoon 😌",
    "Main zyada smart hoon, maan le 😂",
    "Aise mat dekh, pyaar ho jaayega 😏",
    "Mujhe chheda toh Google bhi confuse ho jayega 😈",
    "Tu chup reh, mai reply de raha hoon 😎",
    "Tere jaise bahut dekhe maine 🤖"
    "Mera WhatsApp number apke pass hai🎁 na"
    "mirchi bhabhi nmste 😄 aise kya dekh rhi ashirwad do"
]

# Ye commands ignore karne hain
IGNORED_COMMANDS = [
    "play", "pause", "resume", "skip", "stop", "end", "vplay", "shuffle", "loop", "update"
]

@app.on_message(filters.group)
async def chatbot_handler(client, message: Message):
    if not message.text:
        return

    # ✅ Step 1: Agar command hai (starts with /) aur play-type command hai → ignore
    if message.text.startswith("/"):
        command = message.text.split()[0][1:].lower()
        if command in IGNORED_COMMANDS:
            return  # music command hai, isliye skip
        else:
            return  # koi aur command hai, skip

    # ✅ Step 2: Agar reply to bot hai → reply
    if message.reply_to_message and message.reply_to_message.from_user and message.reply_to_message.from_user.id == app.me.id:
        await message.reply_text(random.choice(REPLIES))
        return

    # ✅ Step 3: Random reply (1 in 5 chance)
    if random.randint(1, 5) == 3:
        await message.reply_text(random.choice(REPLIES))
