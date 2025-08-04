from aiogram import Bot, types
from aiogram.exceptions import TelegramAPIError
from config import ADMIN_IDS

async def notify_admins_about_vacancy(bot: Bot, vacancy: dict, index: int):
    text = (
        "✅ <b>Yangi vakansiya!</b>\n\n"
        f"📞 <b>Telefon:</b> {vacancy.get('contact', 'Nomaʼlum')}\n"
        f"📌 <b>Lavozim:</b> {vacancy.get('title', 'Nomaʼlum')}\n"
        f"🏙 <b>Shahar:</b> {vacancy.get('city', 'Nomaʼlum')}\n"
        f"📝 <b>Tavsif:</b> {vacancy.get('description', 'Yo‘q')}\n"
        f"🆔 <b>Foydalanuvchi ID:</b> <code>{vacancy.get('user_id', 'Nomaʼlum')}</code>"
    )

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=f"approve_{index}"),
        types.InlineKeyboardButton(text="❌ Rad etish", callback_data=f"reject_{index}")
    )

    for admin_id in ADMIN_IDS:
        try:
            await bot.send_message(
                chat_id=admin_id,
                text=text,
                reply_markup=keyboard,
                parse_mode="HTML"
            )
        except TelegramAPIError as e:
            print(f"Telegram API xatosi: {e}")
        except Exception as e:
            print(f"❗️Adminga yuborishda xato: {e}")