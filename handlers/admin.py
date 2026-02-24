from aiogram import types
from config import ADMIN_IDS
from database import load_db, save_db


db = load_db()

def register_admin_handlers(dp):

    @dp.message(lambda m: m.video and m.from_user.id in ADMIN_IDS)
    async def admin_upload(msg: types.Message):

        movie_code = msg.caption.strip() if msg.caption else None
        if not movie_code:
            return await msg.answer("❗ Add movie code in caption!")

        file_id = msg.video.file_id

        # Create entry if needed
        if movie_code not in db:
            db[movie_code] = {}

        # Default: store as 720p
        db[movie_code]["720"] = file_id

        save_db(db)

        await msg.answer(f"🎬 Saved!\nCode: {movie_code}\nQuality: 720p stored!")