from aiogram import Bot
from config import ADMINS
from keyboards.inline import get_admin_approval_keyboard

async def send_to_admins(bot: Bot, vacancy: dict, index: int):
    text = f"<b>Yangi e'lon:</b>\n\n"
    text += f"📌 Lavozim: {vacancy['title']}\n"
    text += f"📍 Shahar: {vacancy['city']}\n"
    text += f"📝 Tavsif: {vacancy['description']}\n"
    text += f"📞 Aloqa: {vacancy['contact']}\n"

    keyboard = get_admin_approval_keyboard(index)
    for admin_id in ADMINS:
        await bot.send_message(chat_id=admin_id, text=text, reply_markup=keyboard, parse_mode="HTML")
