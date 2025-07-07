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
    LOGGER(__name__).info("✅ Chatbot module loaded successfully.")
except ImportError:
    LOGGER(__name__).warning("⚠️ Chatbot module not found. Skipping...")

async def init():
    # ✅ Assistant STRING check
    if not (
        config.STRING1 or config.STRING2 or config.STRING3 or
        config.STRING4 or config.STRING5
    ):
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
        LOGGER(__name__).warning(f"⚠️ Error fetching banned users: {e}")

    # ✅ Start clients
    await app.start()
    await userbot.start()

    # ✅ Import all plugin modules
    for all_module in ALL_MODULES:
        importlib.import_module(f"BrandrdXMusic.plugins.{all_module}")
    LOGGER("BrandrdXMusic.plugins").info("✅ All modules loaded successfully.")

    # ✅ Start PyTgCalls (voice/video)
    await Hotty.start()

    # ✅ Try dummy stream
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("BrandrdXMusic").error(
            "❌ Group video call not started.\nStart a call in log group and restart bot."
        )
        exit()
    except Exception as e:
        LOGGER("BrandrdXMusic").warning(f"⚠️ Stream setup skipped: {e}")

    await Hotty.decorators()
    LOGGER("BrandrdXMusic").info("✅ Music Bot started. Chat + Play working!")

    await idle()

    # ✅ Shutdown
    await app.stop()
    await userbot.stop()
    LOGGER("BrandrdXMusic").info("🛑 Bot stopped cleanly.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
