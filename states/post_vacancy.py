from aiogram.fsm.state import State, StatesGroup

class PostVacancy(StatesGroup):
    title = State()
    city = State()
    description = State()
    contact = State()
