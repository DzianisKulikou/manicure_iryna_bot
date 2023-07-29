from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import lexicon_dict_ru


# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на все сообщения, которые не отловят остальные хэндлеры
@router.message()
async def send_echo(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['unknown_message'])
