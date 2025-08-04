from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def user_menu():
    keyboard = [
        [KeyboardButton(text="📤 Vakansiya joylash")],
        [KeyboardButton(text="📋 Vakansiyalarni ko‘rish")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

def phone_request():
    keyboard = [
        [KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True)
