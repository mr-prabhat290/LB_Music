@Client.on_callback_query(filters.regex("LiveStream") & ~BANNED_USERS)
@languageCB
async def play_live_stream(client, CallbackQuery):
    try:
        user_id = CallbackQuery.from_user.id
        user_name = CallbackQuery.from_user.first_name
        chat_id = CallbackQuery.message.chat.id

        data = CallbackQuery.data.strip().split(None, 1)[1]
        vidid, uid, mode, cplay, fplay = data.split("|")

        if int(uid) != user_id:
            return await CallbackQuery.answer("You're not authorized to use this button.", show_alert=True)

        channel = await get_channelplayCB(_, cplay, CallbackQuery)
        if not channel:
            return

        mystic = await CallbackQuery.message.reply_text(
            _["play_2"].format(channel) if channel else _["play_1"]
        )

        details, track_id = await YouTube.track(vidid, video=True)
        if not details:
            return await mystic.edit_text(_["play_3"])

        if details["duration_min"] and details["duration_min"] != "0":
            return await mystic.edit_text("Not a valid live stream.")

        await stream(
            mystic=mystic,
            chat_id=chat_id,
            user_name=user_name,
            user_id=user_id,
            video=True,
            streamtype="live",
            forceplay=fplay
        )

    except Exception as e:
        err = f"⚠️ Error: `{type(e).__name__}`\n➤ {e}"
        await mystic.edit_text(err)
        await CallbackQuery.answer("Error occurred.", show_alert=True)
    finally:
        await mystic.delete()
