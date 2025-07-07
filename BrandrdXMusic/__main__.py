import asyncio
import importlib
from pyrogram import idle
from pyrogram.errors import UserNotParticipant
from pytgcalls.exceptions import NoActiveGroupCall

import config
from BrandrdXMusic import LOGGER, app, userbot
from BrandrdXMusic.core.call import Hotty
from BrandrdXMusic.plugins import ALL_MODULES
from BrandrdXMusic.utils.database import get_banned_users
from config import BANNED_USERS

# ✅ Optional: Chatbot import (ignore if module missing)
try:
    from BrandrdXMusic.modules import chatbot
except:
    pass

async def init():
    # ✅ Check assistant string availability
    if not any((
        config.STRING1,
        config.STRING2,
        config.STRING3,
        config.STRING4,
        config.STRING5,
    )):
        LOGGER(__name__).error("❌ No assistant STRING1–5 found. Bot shutting down...")
        exit()

    # ✅ Add banned users
    try:
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER(__name__).warning(f"⚠️ Failed to fetch banned users: {e}")

    # ✅ Import all plugin modules
    for module in ALL_MODULES:
        importlib.import_module(f"BrandrdXMusic.plugins.{module}")
    LOGGER("BrandrdXMusic.plugins").info("✅ All Modules Loaded Successfully.")

    # ✅ Start clients
    await userbot.start()
    await Hotty().start()
    await app.start()

    # ✅ Optional: Dummy stream test
    try:
        await Hotty().stream_call("https://graph.org/file/e9959c40cb70067c84b75.mp4")
    except NoActiveGroupCall:
        LOGGER("BrandrdXMusic").error("❌ Group video call not started.\nStart it manually in the log group.")
        exit()
    except Exception as e:
        LOGGER("BrandrdXMusic").warning(f"⚠️ Dummy stream skipped: {e}")

    await idle()

    # ✅ Shutdown on stop
    await userbot.stop()
    await app.stop()
    LOGGER("BrandrdXMusic").info("✅ Bot Stopped Cleanly.")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
