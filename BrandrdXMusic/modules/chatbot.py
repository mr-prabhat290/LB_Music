# BrandrdXMusic/modules/chatbot.py

import aiohttp
import random
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import app

GPT_API = "https://chatgpt.apinepdev.workers.dev/?question="

# Funny savage lines (gali-vibe)
SAVAGE_LINES = [
    "Teri gf ko le gaya, ab kya karega? 💃",
    "Apna mooh dhoke aa pehle 😏",
    "Aukat se baat kar chomu 😎",
    "Baklol ho kya tum full? 😂",
    "Bheja fry ho gaya tera to 😹",
    "Mujhe sunke tera dimaag hil gaya na? 🤯",
    "Tu internet ka dard hai bhai 💀",
    "Logic ki talaash me bhatakta aatma lag raha hai tu 👻",
]

# Telegram sticker file_ids (replace with your own if needed)
STICKERS = [
    "https://t.me/addstickers/ROMMMMMAAANNN_by_fStikBot",  # angry emoji
    "https://t.me/addstickers/kang_6843180470video_by_Sticker_kang_robot",  # funny slap
    "https://t.me/addstickers/Abstract4",  # thinking
    "https://t.me/addstickers/klikhu",  # crying meme
]

# GPT reply with masala
async def gpt_reply(text):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{GPT_API}Reply in short, funny Hindi with emoji: {text}") as resp:
            if resp.status == 200:
                data = await resp.json()
                reply = data.get("answer", "").strip()

                reply = reply.split("🔗")[0].strip()

                if len(reply) > 200:
                    reply = reply[:180] + "..."

                # 30% chance: use savage line
                if random.randint(1, 10) <= 3:
                    reply = random.choice(SAVAGE_LINES)

                return reply + " 😎"
            return "Lagta hai GPT ne bhi teri baat ignore kar di 😂"

# 🔹 DM Chat
@app.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def dm_chat(client, message: Message):
    reply = await gpt_reply(message.text)
    await message.reply_text(reply)

    # 30% chance to send sticker
    if random.randint(1, 10) <= 3:
        sticker_id = random.choice(STICKERS)
        await message.reply_sticker(sticker_id)

# 🔹 Group Chat: Reply to bot or random msg
@app.on_message(filters.group & filters.text)
async def group_chat(client, message: Message):
    bot = await app.get_me()
    if message.from_user.id == bot.id or message.from_user.is_bot:
        return

    # Always reply if message is reply to bot
    if message.reply_to_message and message.reply_to_message.from_user.id == bot.id:
        reply = await gpt_reply(message.text)
        await message.reply_text(reply)
        if random.randint(1, 10) <= 3:
            sticker_id = random.choice(STICKERS)
            await message.reply_sticker(sticker_id)
        return

    # 25% chance to reply randomly
    if random.randint(1, 10) <= 2:
        reply = await gpt_reply(message.text)
        await message.reply_text(reply)
        if random.randint(1, 10) <= 3:
            sticker_id = random.choice(STICKERS)
            await message.reply_sticker(sticker_id)
