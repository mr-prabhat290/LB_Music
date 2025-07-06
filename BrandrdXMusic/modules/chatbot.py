# Free GPT Proxy Chatbot (No OpenAI Key Required)

from pyrogram import filters
from pyrogram.types import Message
import aiohttp
from BrandrdXMusic import app
from config import OWNER_ID

GPT_API = "https://chatgpt.apinepdev.workers.dev/?question="

async def get_gpt_reply(text: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(GPT_API + text) as resp:
            if resp.status == 200:
                data = await resp.text()
                return data.strip()
            else:
                return "❌ GPT API down ya slow hai."

# Private Chat Handler
@app.on_message(filters.private & filters.text & ~filters.command(["start"]))
async def gpt_private(client, message: Message):
    user_text = message.text
    reply = await get_gpt_reply(user_text)
    await message.reply_text(reply)

# Group Chat Handler (when bot is replied to)
@app.on_message(filters.group & filters.reply & filters.text)
async def gpt_group(client, message: Message):
    if message.reply_to_message.from_user.id != (await app.get_me()).id:
        return
    user_text = message.text
    reply = await get_gpt_reply(user_text)
    await message.reply_text(reply)
