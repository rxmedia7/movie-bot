from aiogram import types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import REQUIRED_CHANNELS
from handlers.subscription import check_all_subs


def register_start_handlers(dp):

    @dp.message(Command("start"))
    async def start_cmd(msg: types.Message):

        if not await check_all_subs(msg.from_user.id, msg.bot):
            buttons = []

            for ch in REQUIRED_CHANNELS:
                ch_name = ch.replace("@", "")
                buttons.append([InlineKeyboardButton(
                    text=f"Join {ch_name}",
                    url=f"https://t.me/{ch_name}"
                )])

            buttons.append([InlineKeyboardButton(
                text="✅ I Subscribed",
                callback_data="check_subs"
            )])

            return await msg.answer(
                "❗ Please subscribe to required channels:",
                reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
            )

        await msg.answer("🎬 Send me a movie code")