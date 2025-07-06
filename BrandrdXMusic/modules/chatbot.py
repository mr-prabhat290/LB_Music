# BrandrdXMusic/modules/chatbot.py

import aiohttp
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import app

GPT_API = "https://chatgpt.apinepdev.workers.dev/?question="

# Short + smart GPT reply
async def gpt_reply(text):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{GPT_API}Give a short, casual reply in Hindi: {text}") as resp:
            if resp.status == 200:
                data = await resp.json()
                reply = data.get("answer", "").strip()

                # Clean garbage and trim if too long
                if "t.me/" in reply:
                    reply = reply.split("🔗")[0].strip()
                if len(reply) > 200:
                    reply = reply[:180] + "..."

                # Natural chat feel
                if not reply.endswith("!") and not reply.endswith(".") and not reply.endswith("?"):
                    reply += " 😊"

                return reply
            return "Thoda slow ho gaya hoon lagta hai 😅"

# 🔹 Private chat
@app.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def private_chat(client, message: Message):
    reply = await gpt_reply(message.text)
    await message.reply_text(reply)

# 🔹 Group reply (only if bot is replied to)
@app.on_message(filters.group & filters.text & filters.reply)
async def group_reply_chat(client, message: Message):
    if message.reply_to_message.from_user.id != (await app.get_me()).id:
        return  # Bot ko reply nahi kiya, skip
    reply = await gpt_reply(message.text)
    await message.reply_text(reply)
