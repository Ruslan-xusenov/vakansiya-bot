import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram.client.default import DefaultBotProperties
from config import BOT_TOKEN
from handlers import user, admin
from middlewares.auth import AdminFilter

async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.outer_middleware(AdminFilter())

    dp.include_routers(
        user.router,
        admin.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    print("✅ Bot ishga tushdi.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())