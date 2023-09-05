from aiogram import Router
from aiogram.types import Message

from database.database import users_db
from lexicon.lexicon_en import lexicon_dict_en
from lexicon.lexicon_pl import lexicon_dict_pl
from lexicon.lexicon_ru import lexicon_dict_ru


# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на все сообщения, которые не отловят остальные хэндлеры ru
@router.message()
async def send_echo(message: Message):
    if message.from_user.id == message.chat.id:
        if users_db[message.from_user.id]['language'] == 'ru':
            await message.answer(text=lexicon_dict_ru['unknown_message'])
        elif users_db[message.from_user.id]['language'] == 'en':
            await message.answer(text=lexicon_dict_en['unknown_message'])
        elif users_db[message.from_user.id]['language'] == 'pl':
            await message.answer(text=lexicon_dict_pl['unknown_message'])
        else:
            await message.answer(text=lexicon_dict_ru['unknown_message'])  # если нет языка
