import random import time from pyrogram import filters from pyrogram.types import Message from BrandrdXMusic import app

Store last 20 group messages

recent_messages = [] LAST_REPLY_TIME = 0

Fun replies and stickers

funny_lines = [ "teri gf ko le gaya 😏", "sab chup kyu ho bhai 😐", "kya neend aa gayi sabko? 😂", "kisi ko to farak nahi padta 🥲", "admin chup hai, to hum hi kuch bolte hain 😎", "chalo kuch to bolo, warna bhag jaunga 👻", "teri crush ab meri ho gayi 😌" ]

funny_stickers = [ "https://t.me/addstickers/mrincred", "https://t.me/addstickers/Meme_stickers" ]

Words to ignore (music commands)

IGNORE_KEYWORDS = ["/play", "/skip", "/pause", "/resume", "/stop", "/end", "/join"]

Check if bot should reply

def should_reply(message: Message): global LAST_REPLY_TIME now = time.time()

if message.from_user.is_bot:
    return False

text = message.text.lower()
if any(word in text for word in IGNORE_KEYWORDS):
    return False

if message.reply_to_message and message.reply_to_message.from_user.id == app.id:
    LAST_REPLY_TIME = now
    return True

if now - LAST_REPLY_TIME > 60:
    LAST_REPLY_TIME = now
    return True

if (now - LAST_REPLY_TIME) > 20 and random.randint(1, 10) == 1:
    LAST_REPLY_TIME = now
    return True

return False

Chatbot listener

@app.on_message(filters.group & filters.text & ~filters.via_bot) async def chatbot_group(client, message: Message): recent_messages.append(message.text) if len(recent_messages) > 20: recent_messages.pop(0)

if should_reply(message):
    response = random.choice(funny_lines)
    await message.reply_text(response)

    # 30% chance to send a sticker too
    if random.randint(1, 100) <= 30:
        await message.reply_sticker(random.choice(funny_stickers))

