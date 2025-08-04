from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any
from config import ADMINS

class AdminFilter(BaseMiddleware):
    async def __call__(self, handler: Callable, event: Message, data: Dict[str, Any]) -> Any:
        if event.text and event.text.startswith("/admin"):
            if event.from_user.id not in ADMINS:
                await event.answer("⛔ Sizda bu buyruq uchun ruxsat yo‘q.")
                return
        return await handler(event, data)