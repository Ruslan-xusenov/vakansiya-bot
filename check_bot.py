from aiogram import Bot
from config import BOT_TOKEN
import asyncio

async def check_bot():
    try:
        bot = Bot(token=BOT_TOKEN)
        me = await bot.get_me()
        print(f"✅ Bot username: @{me.username}")
        print(f"👤 Bot name: {me.full_name}")
        print(f"🆔 Bot ID: {me.id}")
    except Exception as e:
        print(f"❌ Botni tekshirishda xatolik: {e}")
    finally:
        await bot.session.close()

asyncio.run(check_bot())
