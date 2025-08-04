from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def city_selection_keyboard() -> InlineKeyboardMarkup:
    cities = ["Toshkent", "Samarqand", "Buxoro", "Farg‘ona", "Andijon"]
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=city, callback_data=f"city_{city}") for city in cities]
    keyboard.add(*buttons)
    return keyboard

def get_admin_approval_keyboard(user_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=f"approve:{user_id}"),
                InlineKeyboardButton(text="❌ Rad etish", callback_data=f"reject:{user_id}")
            ]
        ]
    )

def category_selection_keyboard() -> InlineKeyboardMarkup:
    categories = ["IT", "Marketing", "Savdo", "Retoran", "Yuk tashuvchi"]
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(text=cat, callback_data=f"cat_{cat}") for cat in categories]
    keyboard.add(*buttons)
    return keyboard

def confirmation_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Ha", callback_data="confirm_yes"),
                InlineKeyboardButton(text="❌ Yo‘q", callback_data="confirm_no")
            ]
        ]
    )

def channel_selection_keyboard(channels: list) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    buttons = [InlineKeyboardButton(text=name, callback_data=f"channel_{chat_id}") for name, chat_id in channels]
    keyboard.add(*buttons)
    return keyboard
