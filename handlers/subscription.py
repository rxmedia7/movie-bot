from aiogram import Bot
from aiogram.types import CallbackQuery
from config import REQUIRED_CHANNELS


async def is_subscribed(user_id, channel, bot: Bot):
    try:
        member = await bot.get_chat_member(channel, user_id)
        return member.status not in ["left", "kicked"]
    except:
        return False


async def check_all_subs(user_id, bot: Bot):
    for ch in REQUIRED_CHANNELS:
        if not await is_subscribed(user_id, ch, bot):
            return False
    return True


def register_subscription_handlers(dp):

    @dp.callback_query(lambda c: c.data == "check_subs")
    async def recheck(call: CallbackQuery):

        if await check_all_subs(call.from_user.id, call.bot):
            return await call.message.edit_text("✔️ Subscribed! Now send the movie code.")

        await call.answer("❗ You still haven't subscribed!", show_alert=True)