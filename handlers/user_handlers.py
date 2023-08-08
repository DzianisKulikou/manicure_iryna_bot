from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandStart, Text
from lexicon.lexicon_ru import lexicon_dict_ru
from keyboards.kb_main import keyboard, keyboard_i_2
from keyboards.keyboard_manicure import keyboard_manicure
from keyboards.kb_kontakt import keyboard_kontakt, keyboard_i_1
from database.database import users_db, user_dict_template
from database.database_photo import photo_map
from copy import deepcopy
from aiogram import Bot

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=lexicon_dict_ru['/start'])
    await bot.send_message(chat_id=message.from_user.id, text=lexicon_dict_ru['menu'], reply_markup=keyboard)
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['/help'])


# Этот хэндлер будет срабатывать на кнопку 'Мой адрес'
@router.message(Text(text='Мой адрес'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['adres'])
        await message.answer_photo(photo=FSInputFile(photo_map))


# Этот хэндлер будет срабатывать на кнопку 'Мой контактный телефон'
@router.message(Text(text='Мой контактный телефон'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['phone'])


# Этот хэндлер будет срабатывать на кнопку 'Прайс лист'
@router.message(Text(text='Прайс лист'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['price list'])

# Этот хэндлер будет срабатывать на кнопку 'Написать Ирине в Telegram'
@router.message(Text(text='Написать Ирине в Telegram'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['me'], reply_markup=keyboard_i_1)


# Этот хэндлер будет срабатывать на кнопку 'Вся информация о работе мастера'
@router.message(Text(text='Вся информация о работе мастера'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['start_manicure'], reply_markup=keyboard_manicure)


# Этот хэндлер будет срабатывать на кнопку 'Мои контактные данные'
@router.message(Text(text='Мои контактные данные'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['kontakt'], reply_markup=keyboard_kontakt)


# Этот хэндлер будет срабатывать на кнопку 'Вернуться в главное меню' [button_10]
@router.message(Text(text='Вернуться в главное меню'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['start_menu'], reply_markup=keyboard)


# Этот хэндлер будет срабатывать на кнопку 'Информация о разработчике бота' [button_100]
@router.message(Text(text='Информация о разработчике бота'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['developer'], reply_markup=keyboard_i_2)
