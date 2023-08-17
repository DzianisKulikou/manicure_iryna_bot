from aiogram import Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command, CommandStart, Text

from lexicon.lexicon_pl import lexicon_dict_pl
from lexicon.lexicon_ru import lexicon_dict_ru, lexicon_certificates
from lexicon.lexicon_en import lexicon_dict_en
from keyboards.kb_main import *
from keyboards.keyboard_manicure import *
from keyboards.kb_kontakt import *
from database.database import users_db, user_dict_template
from database.database_photo import photo_map
from copy import deepcopy
from aiogram import Bot


# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text=lexicon_dict_ru['/start'], reply_markup=keyboard_in_lg)
    print(message.chat.id, message.from_user.id, message.from_user.full_name)  # id chat, id user, name user
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Русский"
@router.callback_query(Text(text='button_in_lg1'))
async def process_button_in_1(callback: CallbackQuery):
    users_db[callback.from_user.id]['language'] = 'ru'
    await callback.message.answer(text=lexicon_dict_ru['start'])
    await callback.message.answer(text=lexicon_dict_ru['menu'], reply_markup=keyboard)
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "English"
@router.callback_query(Text(text='button_in_lg2'))
async def process_button_in_1(callback: CallbackQuery):
    users_db[callback.from_user.id]['language'] = 'en'
    await callback.message.answer(text=lexicon_dict_en['start'])
    await callback.message.answer(text=lexicon_dict_en['menu'], reply_markup=keyboard_en)
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Polski"
@router.callback_query(Text(text='button_in_lg3'))
async def process_button_in_1(callback: CallbackQuery):
    users_db[callback.from_user.id]['language'] = 'pl'
    await callback.message.answer(text=lexicon_dict_pl['start'])
    await callback.message.answer(text=lexicon_dict_pl['menu'], reply_markup=keyboard_pl)
    await callback.answer()


# @router.message(CommandStart())
# async def process_start_command(message: Message, bot: Bot):
#     await bot.send_message(chat_id=message.from_user.id, text=lexicon_dict_ru['/start'])
#     await bot.send_message(chat_id=message.from_user.id, text=lexicon_dict_ru['menu'], reply_markup=keyboard)
#     if message.from_user.id not in users_db:
#         users_db[message.from_user.id] = deepcopy(user_dict_template)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    if message.from_user.id == message.chat.id:
        if users_db[message.from_user.id]['language'] == 'ru':
            await message.answer(text=lexicon_dict_ru['/help'])
        elif users_db[message.from_user.id]['language'] == 'en':
            await message.answer(text=lexicon_dict_en['/help'])
        elif users_db[message.from_user.id]['language'] == 'pl':
            await message.answer(text=lexicon_dict_pl['/help'])


# Этот хэндлер будет срабатывать на кнопку 'Мой адрес' [button_1]
@router.message(Text(text='Мой адрес'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['adres'])
        await message.answer_photo(photo=FSInputFile(photo_map))


# Этот хэндлер будет срабатывать на кнопку 'Мой контактный телефон' [button_2]
@router.message(Text(text='Мой контактный телефон'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['phone'])


# Этот хэндлер будет срабатывать на кнопку 'Прайс лист' [button_8]
@router.message(Text(text='Прайс лист'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['price list'])


# Этот хэндлер будет срабатывать на кнопку 'Мои сертификаты' [button_12]
@router.message(Text(text='Мои сертификаты'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_certificates['cer'])
        await message.answer(text=lexicon_certificates['cer1'])


# Этот хэндлер будет срабатывать на кнопку 'Написать Ирине в Telegram' [button_5]
@router.message(Text(text='Написать Ирине в Telegram'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['me'], reply_markup=keyboard_i_1)


# Этот хэндлер будет срабатывать на кнопку 'Вся информация о работе мастера' [button_6]
@router.message(Text(text='Вся информация о работе мастера'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['start_manicure'], reply_markup=keyboard_manicure)


# Этот хэндлер будет срабатывать на кнопку 'Мои контактные данные' [button_9]
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
