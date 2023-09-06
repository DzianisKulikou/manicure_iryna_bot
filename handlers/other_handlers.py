from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.database import users_db, user_dict_template
from keyboards.kb_main import keyboard_in_lg
from lexicon.lexicon_en import lexicon_dict_en
from lexicon.lexicon_pl import lexicon_dict_pl
from lexicon.lexicon_ru import lexicon_dict_ru


# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на все сообщения, которые не отловят остальные хэндлеры ru
@router.message()
async def send_echo(message: Message, bot=None):
    if message.from_user.id == message.chat.id:
        if message.from_user.id not in users_db:
            await bot.send_message(chat_id=message.from_user.id,
                                   text='Бот был перезапущен, для корректной работы нажмите: /start')
        elif users_db[message.from_user.id]['language'] == 'ru':
            await message.answer(text=lexicon_dict_ru['unknown_message'])
        elif users_db[message.from_user.id]['language'] == 'en':
            await message.answer(text=lexicon_dict_en['unknown_message'])
        elif users_db[message.from_user.id]['language'] == 'pl':
            await message.answer(text=lexicon_dict_pl['unknown_message'])
