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

# ✅ Optional: Chatbot module auto-load (if chatbot.py is in modules, not plugins)
try:
    from BrandrdXMusic.modules import chatbot
except:
    pass  # Safe ignore if not needed

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER(__name__).warning(f"Failed to fetch banned users: {e}")

    # ✅ Start bot, plugins, assistant, and call
    await app.start()

    # ✅ CORRECTED plugin import:
    for all_module in ALL_MODULES:
        importlib.import_module(f"BrandrdXMusic.plugins.{all_module}")
    LOGGER("BrandrdXMusic.plugins").info("Successfully Imported Modules...")

    await userbot.start()
    await Hotty.start()

    # ✅ Attempt to pre-stream a placeholder to warm up call (optional)
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("BrandrdXMusic").error(
            "Please turn on the videochat of your log group/channel.\nStopping Bot..."
        )
        exit()
    except Exception as e:
        LOGGER("BrandrdXMusic").warning(f"Stream call error: {e}")

    await Hotty.decorators()
    LOGGER("BrandrdXMusic").info(
        "ʙᴏᴛ ɪꜱ ʀᴇᴀᴅʏ! ᴊᴏɪɴ @ruthlesszone & @MusicXpressBot ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ"
    )

    await idle()

    # Shutdown gracefully
    await app.stop()
    await userbot.stop()
    LOGGER("BrandrdXMusic").info("Stopping Brandrd Music Bot...")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
