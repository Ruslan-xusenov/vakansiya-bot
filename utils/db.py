import json
import os
import asyncio
from datetime import datetime
from config import VACANCIES_FILE
from utils.posting import send_to_admins

lock = asyncio.Lock()

async def load_vacancies():
    if not os.path.exists(VACANCIES_FILE):
        return []
    try:
        with open(VACANCIES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []

async def save_all_vacancies(vacancies: list):
    async with lock:
        with open(VACANCIES_FILE, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, indent=4, ensure_ascii=False)

async def save_vacancy(data, user_id: int, bot):
    # Bu yerda siz faylga yoki bazaga yozishingiz mumkin
    with open("vacancies.json", "a", encoding="utf-8") as f:
        f.write(json.dumps({"user_id": user_id, **data}, ensure_ascii=False) + "\n")

    await send_to_admins(bot, data, user_id)
