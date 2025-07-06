# BrandrdXMusic/modules/chatbot.py

import aiohttp
from pyrogram import filters
from pyrogram.types import Message
from BrandrdXMusic import app

GPT_API = "https://chatgpt.apinepdev.workers.dev/?question="

async def gpt_reply(text):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{GPT_API}{text}") as resp:
            if resp.status == 200:
                data = await resp.json()
                reply = data.get("answer", "").strip()
                if "t.me/" in reply:
                    reply = reply.split("🔗")[0].strip()
                if reply.endswith("."):
                    reply += " 😊"
                elif "?" in reply:
                    reply += " 🤔"
                else:
                    reply += " 😄"
                return reply
            return "GPT busy hai bhai 😴"

# 🔹 Private ChatBot (DM)
@app.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def dm_chat(client, message: Message):
    reply = await gpt_reply(message.text)
    await message.reply_text(reply)

# 🔹 Group ChatBot (Public Mode – every message)
@app.on_message(filters.group & filters.text & ~filters.command(["start"]))
async def public_group_chat(client, message: Message):
    if message.from_user.is_bot:
        return  # Bot ko ignore karo
    reply = await gpt_reply(message.text)
    await message.reply_text(reply)
