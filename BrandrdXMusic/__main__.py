import asyncio
import importlib
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from BrandrdXMusic import LOGGER, app, userbot
from BrandrdXMusic.core.call import Hotty
from BrandrdXMusic.misc import sudo
from BrandrdXMusic.plugins import ALL_MODULES
from BrandrdXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

# ✅ Optional: Load chatbot module if exists
try:
    from BrandrdXMusic.modules import chatbot
except:
    pass  # Chatbot not mandatory

async def init():
    # ✅ Assistant session string check
    if not any([
        config.STRING1,
        config.STRING2,
        config.STRING3,
        config.STRING4,
        config.STRING5
    ]):
        LOGGER(__name__).error("❌ No assistant STRING1–5 found. Bot shutting down...")
        exit()

    # ✅ Add banned users
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER(__name__).warning(f"❗Error fetching banned users: {e}")

    # ✅ Start main bot
    await app.start()

    # ✅ Import all plugin modules (FIXED)
    for all_module in ALL_MODULES:
        importlib.import_module(f"BrandrdXMusic.plugins.{all_module}")
    LOGGER("BrandrdXMusic.plugins").info("✅ All Modules Loaded Successfully.")

    # ✅ Start assistant client (userbot)
    await userbot.start()

    # ✅ Start PyTgCalls (voice/video)
    await Hotty.start()

    # ✅ Try dummy stream (optional)
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("BrandrdXMusic").error(
            "❌ Group video call not started!\nStart a call in log group and restart bot."
        )
        exit()
    except Exception as e:
        LOGGER("BrandrdXMusic").warning(f"Stream setup skipped: {e}")

    await Hotty.decorators()

    LOGGER("BrandrdXMusic").info("🎧 Music Bot Started. Drop issues at @ruthlesszone")
    await idle()

    # ✅ Stop cleanly on shutdown
    await app.stop()
    await userbot.stop()
    LOGGER("BrandrdXMusic").info("Bot Stopped Cleanly.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
