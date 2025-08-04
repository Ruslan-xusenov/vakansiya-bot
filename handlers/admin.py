from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from utils.db import load_vacancies, save_all_vacancies
from aiogram.exceptions import TelegramBadRequest

router = Router()

@router.callback_query(F.data.startswith("approve:"))
async def handle_approve(call: CallbackQuery, bot: Bot):
    user_id = int(call.data.split(":")[1])
    await call.message.edit_reply_markup()
    await call.answer("Tasdiqlandi ✅")

    try:
        await bot.send_message(user_id, "🎉 Sizning e’loningiz admin tomonidan tasdiqlandi va kanalga joylandi.")
        await bot.send_message(call.message.chat.id, "✅ E’lon tasdiqlandi.")
    except TelegramBadRequest:
        pass

@router.callback_query(F.data.startswith("reject:"))
async def handle_reject(call: CallbackQuery, bot: Bot):
    user_id = int(call.data.split(":")[1])
    await call.message.edit_reply_markup()
    await call.answer("Rad etildi ❌")

    try:
        await bot.send_message(user_id, "😔 Kechirasiz, e’loningiz admin tomonidan rad etildi.")
        await bot.send_message(call.message.chat.id, "❌ E’lon rad etildi.")
    except TelegramBadRequest:
        pass