# BrandrdXMusic/modules/chatbot.py

import aiohttp
import random
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import app

GPT_API = "https://chatgpt.apinepdev.workers.dev/?question="

# 🔞 Fun Mode Lines (masaledar + funny)
SAVAGE_LINES = [
    "Teri gf ko leke bhag jaunga 💃",
    "Apna dimaag leke aa pehle, fir baat kar 🤓",
    "Tera level to Nokia 1100 hai bhai 😎",
    "Bakwaas band kar aur chai le aa ☕",
    "Tujhse zyada intelligent to mere shoes hain 👟",
    "Mujhe lagta hai tu chhota packet bada drama hai 😂",
    "Tera logic sunke AC bhi garam ho gaya 🔥",
    "Chal nikal, aur bhi kaam hai mujhe 😏",
    "Main AI hoon, tu human — beizzati fix hai 😹",
    "Tumhari aukaat Telegram ke spam folder jaisi hai 📂",
]

# GPT reply fetcher
async def gpt_reply(text):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{GPT_API}Give a short, sarcastic or witty Hindi reply with emojis: {text}") as resp:
            if resp.status == 200:
                data = await resp.json()
                reply = data.get("answer", "").strip()

                # Clean link junk
                reply = reply.split("🔗")[0].strip()

                # 30% chance: savage line
                if random.randint(1, 10) <= 3:
                    reply = random.choice(SAVAGE_LINES)

                if len(reply) > 220:
                    reply = reply[:180] + "..."

                return reply + " 😎"
            return "Sochne ka kaam chhod de bhai, tu confuse karega 😵"

# 🔹 Private Chat (DM)
@app.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def dm_chat(client, message: Message):
    reply = await gpt_reply(message.text)
    await message.reply_text(reply)

# 🔹 Group Chat (reply OR random mode)
@app.on_message(filters.group & filters.text)
async def group_chat(client, message: Message):
    bot = await app.get_me()
    if message.from_user.id == bot.id or message.from_user.is_bot:
        return

    # Always reply if bot is replied to
    if message.reply_to_message and message.reply_to_message.from_user.id == bot.id:
        reply = await gpt_reply(message.text)
        return await message.reply_text(reply)

    # 25% chance: bot replies randomly
    if random.randint(1, 10) <= 2:
        reply = await gpt_reply(message.text)
        return await message.reply_text(reply)
