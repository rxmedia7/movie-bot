import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.start import register_start_handlers
from handlers.subscription import register_subscription_handlers
from handlers.movies import register_movie_handlers
from handlers.admin import register_admin_handlers

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Register handlers
    register_start_handlers(dp)
    register_subscription_handlers(dp)
    register_movie_handlers(dp)
    register_admin_handlers(dp)

    print("Bot is running…")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())