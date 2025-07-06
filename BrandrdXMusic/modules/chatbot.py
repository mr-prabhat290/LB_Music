# BrandrdXMusic/modules/chatbot.py

from pyrogram import filters
from pyrogram.types import Message
import openai
from BrandrdXMusic import app
from config import OPENAI_API_KEY, OWNER_ID

openai.api_key = OPENAI_API_KEY

# Private Chat AI Handler
@app.on_message(filters.private & filters.text & ~filters.bot)
async def private_chat(client, message: Message):
    await ai_reply(message)

# Group Chat AI Handler (only when bot is replied to)
@app.on_message(filters.group & filters.text & filters.reply)
async def group_chat(client, message: Message):
    if message.reply_to_message.from_user.id == (await client.get_me()).id:
        await ai_reply(message)

# AI Reply Handler
async def ai_reply(message: Message):
    try:
        input_text = message.text.strip()
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": input_text}]
        )
        reply_text = res.choices[0].message.content.strip()
        await message.reply_text(reply_text)
    except Exception as e:
        await message.reply_text(f"🚫 Error:\n{e}")
