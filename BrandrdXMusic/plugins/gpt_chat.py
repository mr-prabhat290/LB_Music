from pyrogram import Client, filters
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

@Client.on_message(filters.private & filters.text & ~filters.command(["start", "help", "play"]))
async def gpt_reply(client, message):
    try:
        user_input = message.text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        reply = response['choices'][0]['message']['content']
        await message.reply_text(reply)
    except Exception as e:
        await message.reply_text(f"❌ Error:\n`{str(e)}`")
