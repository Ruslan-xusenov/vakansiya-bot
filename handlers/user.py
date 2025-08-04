import json
from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CITIES_FILE, ADMINS
from keyboards.default import phone_request, user_menu
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

router = Router()


class PostVacancy(StatesGroup):
    phone = State()
    title = State()
    city = State()
    description = State()


def city_selection_keyboard(cities: list[str]) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text=city, callback_data=f"city:{city}")]
        for city in cities
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\nVakansiya botiga xush kelibsiz!",
        reply_markup=user_menu()
    )


@router.message(F.text == "📤 Vakansiya joylash")
async def ask_phone(message: Message, state: FSMContext):
    await message.answer("📞 Telefon raqamingizni yuboring:", reply_markup=phone_request())
    await state.set_state(PostVacancy.phone)


@router.message(PostVacancy.phone, F.contact)
async def ask_title(message: Message, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone=phone_number)
    await message.answer("📌 Ish nomini kiriting:")
    await state.set_state(PostVacancy.title)


@router.message(PostVacancy.phone)
async def ask_title_text(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("📌 Ish nomini kiriting:")
    await state.set_state(PostVacancy.title)


@router.message(PostVacancy.title)
async def ask_city(message: Message, state: FSMContext):
    await state.update_data(title=message.text)

    try:
        with open(CITIES_FILE, "r") as f:
            cities = json.load(f)
    except:
        cities = ["Toshkent", "Samarqand", "Buxoro", "Andijon"]

    await message.answer("🏙 Iltimos, shaharni tanlang:", reply_markup=city_selection_keyboard(cities))


@router.callback_query(F.data.startswith("city:"))
async def handle_city_selection(call: CallbackQuery, state: FSMContext):
    selected_city = call.data.split(":")[1]
    await state.update_data(city=selected_city)

    await call.message.delete()

    await call.message.answer(f"✅ Shahar tanlandi: <b>{selected_city}</b>", parse_mode="HTML")
    await call.message.answer("📝 Iltimos, ish tavsifini kiriting:")
    await state.set_state(PostVacancy.description)

def get_approval_keyboard(user_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=f"approve:{user_id}"),
                InlineKeyboardButton(text="❌ Rad etish", callback_data=f"reject:{user_id}"),
            ]
        ]
    )


@router.message(PostVacancy.description)
async def save_vacancy(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()

    text = (
        f"<b>✅ Yangi vakansiya!</b>\n\n"
        f"<b>📞 Telefon:</b> {data['phone']}\n"
        f"<b>📌 Lavozim:</b> {data['title']}\n"
        f"<b>🏙 Shahar:</b> {data['city']}\n"
        f"<b>📝 Tavsif:</b> {data['description']}"
    )

    keyboard = get_approval_keyboard(user_id=message.from_user.id)

    for admin_id in ADMINS:
        try:
            await message.bot.send_message(
                admin_id,
                text,
                parse_mode=ParseMode.HTML,
                reply_markup=keyboard
            )
        except Exception as e:
            print(f"Xatolik: {e}")

    await message.answer("✅ Vakansiyangiz muvoffaqiyatli yuborildi! Adminlar tasdiqlashi kutilmoqda.")
    await state.clear()