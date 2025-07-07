import aiohttp import os import json import random from pyrogram import filters from pyrogram.types import Message from BrandrdXMusic import app

GPT_API = "https://chatgpt.apinepdev.workers.dev/?question=" MEMORY_FOLDER = "memory" MAX_MEMORY = 20 STICKERS = [ "CAACAgUAAxkBAAEBUn5mYzhqlY7OPZznUCM1nNdqd_j13AACmgEAAhZCAVQzY_Pm7kphqDUE", "CAACAgUAAxkBAAEBUoFmYzjNjKoQ5HdYbFWWaQnLvXWWPwACcAEAAhZCAVTwKxT8vpgPMjUE", "CAACAgUAAxkBAAEBUoNmYzjfCNq6gQH8TVgFvSOPvVDFjQACWwEAAhZCAVTXqDE_qZhVKjUE", "CAACAgUAAxkBAAEBUoVmYzjntoCluLJ5IM9hZn7-5uO3DwACbgEAAhZCAVSV6OSpsLz7ezUE", ] SAVAGE_LINES = [ "Teri gf ko le gaya, ab kya karega? 💃", "Apna mooh dhoke aa pehle 😏", "Aukat se baat kar chomu 😎", "Baklol ho kya tum full? 😂", "Tu internet ka dard hai bhai 💀", ]

Ensure memory folder exists

os.makedirs(MEMORY_FOLDER, exist_ok=True)

Save recent group messages

def save_message(chat_id, user, text): file_path = os.path.join(MEMORY_FOLDER, f"{chat_id}.json") data = [] if os.path.exists(file_path): with open(file_path, "r") as f: data = json.load(f) data.append({"user": user, "text": text}) data = data[-MAX_MEMORY:] with open(file_path, "w") as f: json.dump(data, f)

Get memory context

def get_memory(chat_id): file_path = os.path.join(MEMORY_FOLDER, f"{chat_id}.json") if not os.path.exists(file_path): return "" with open(file_path, "r") as f: data = json.load(f) context = "\n".join([f"{m['user']}: {m['text']}" for m in data]) return context

GPT fetch with memory context

async def gpt_reply(context, user_input): prompt = f"Group Chat:\n{context}\nNow reply to: "{user_input}"" async with aiohttp.ClientSession() as session: async with session.get(GPT_API + prompt) as resp: if resp.status == 200: data = await resp.json() reply = data.get("answer", "...").split("🔗")[0].strip() if random.randint(1, 10) <= 3: reply = random.choice(SAVAGE_LINES) return reply + " 😎" return "Lagta hai GPT ne bhi ignore maar diya 😂"

Handle DM

@app.on_message(filters.private & filters.text & ~filters.command(["start"])) async def private_chat(client, message: Message): reply = await gpt_reply("", message.text) await message.reply_text(reply) if random.randint(1, 10) <= 3: await message.reply_sticker(random.choice(STICKERS))

Handle Group

@app.on_message(filters.group & filters.text) async def group_chat(client, message: Message): bot = await app.get_me() if message.from_user.id == bot.id or message.from_user.is_bot: return

save_message(message.chat.id, message.from_user.first_name, message.text)
context = get_memory(message.chat.id)

# Always respond if replied
if message.reply_to_message and message.reply_to_message.from_user.id == bot.id:
    reply = await gpt_reply(context, message.text)
    await message.reply_text(reply)
    if random.randint(1, 10) <= 3:
        await message.reply_sticker(random.choice(STICKERS))
    return

# Random reply mode (20% chance)
if random.randint(1, 10) <= 2:
    reply = await gpt_reply(context, message.text)
    await message.reply_text(reply)
    if random.randint(1, 10) <= 3:
        await message.reply_sticker(random.choice(STICKERS))

