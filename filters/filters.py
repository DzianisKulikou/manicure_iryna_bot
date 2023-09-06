from aiogram.filters import BaseFilter
from aiogram.types import Message

from database.database import users_db


# Собственный фильтр, проверяющий юзера на наличие в базе
class IsBase(BaseFilter):
    def __init__(self, users_db: dict) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.users_db = users_db

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in users_db
