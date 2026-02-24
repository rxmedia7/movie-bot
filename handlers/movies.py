from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import load_db


db = load_db()

def register_movie_handlers(dp):

    @dp.message(lambda m: m.text and not m.video)
    async def movie_request(msg: types.Message):

        code = msg.text.strip()

        if code not in db:
            return await msg.answer("❗ Movie not found")

        # Create quality menu
        buttons = []
        for q in db[code]:
            buttons.append([
                InlineKeyboardButton(
                    text=f"{q}p",
                    callback_data=f"quality_{code}_{q}"
                )
            ])

        await msg.answer(
            "Select quality:",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
        )

    @dp.callback_query(lambda c: c.data.startswith("quality_"))
    async def send_movie(call: types.CallbackQuery):

        _, code, q = call.data.split("_")

        file_id = db[code][q]

        await call.message.answer_video(video=file_id)
        await call.answer()