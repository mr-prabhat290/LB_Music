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

                # ✨ Emoji touch here
                if reply.endswith("."):
                    reply += " 😊"
                elif "?" in reply:
                    reply += " 🤔"
                else:
                    reply += " 😄"
                return reply
            return "Kya bolu bhai, GPT so gaya lagta hai 😴"

# DM chatbot
@app.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def dm_chat(client, message: Message):
    reply = await gpt_reply(message.text)
    await message.reply_text(reply)

# Group chatbot (only if someone replies to bot)
@app.on_message(filters.group & filters.text & filters.reply)
async def group_chat(client, message: Message):
    if message.reply_to_message.from_user.id != (await app.get_me()).id:
        return
    reply = await gpt_reply(message.text)
    await message.reply_text(reply)
