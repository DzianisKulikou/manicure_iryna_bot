from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, FSInputFile

from database.database import users_db
from database.database_photo import photo_map, photo_certificates
from filters.filters import IsBase
from keyboards.kb_kontakt import *
from keyboards.kb_main import *
from keyboards.keyboard_manicure import *
from keyboards.pagination_kb import create_pagination_kb_ser
from lexicon.lexicon_en import lexicon_dict_en, lexicon_certificates_en

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на кнопку 'My address' [button_1]
@router.message(Text(text='My address'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_en['adres'])
        await message.answer_photo(photo=FSInputFile(photo_map))


# Этот хэндлер будет срабатывать на кнопку 'My contact phone number' [button_2]
@router.message(Text(text='My contact phone number'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_en['phone'])


# Этот хэндлер будет срабатывать на кнопку 'Price list' [button_8]
@router.message(Text(text='Price list'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_en['price list'])


# Этот хэндлер будет срабатывать на кнопку 'My Certificates' [button_12]
@router.message(Text(text='My Certificates'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_certificates_en['cer'])
        await message.answer(text=lexicon_certificates_en['cer1'])
        index_photo = users_db[message.from_user.id]['page_certificates']
        await message.answer_photo(
            photo=FSInputFile(photo_certificates[index_photo]),
            reply_markup=create_pagination_kb_ser(
                'backward_cer',
                f'{users_db[message.from_user.id]["page_certificates"]}/{len(photo_certificates)}',
                'forward_cer'))


# Этот хэндлер будет срабатывать на кнопку 'Write to me in Telegram' [button_5]
@router.message(Text(text='Write to me in Telegram'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_en['me'], reply_markup=keyboard_i_1_en)


# Этот хэндлер будет срабатывать на кнопку 'All information about the work of the wizard' [button_6]
@router.message(Text(text='All information about the work of the wizard'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_en['start_manicure'], reply_markup=keyboard_manicure_en)


# Этот хэндлер будет срабатывать на кнопку 'My contact details' [button_9]
@router.message(Text(text='My contact details'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_en['kontakt'], reply_markup=keyboard_kontakt_en)


# Этот хэндлер будет срабатывать на кнопку 'Go back to the main menu' [button_10]
@router.message(Text(text='Go back to the main menu'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_en['start_menu'], reply_markup=keyboard_en)


# Этот хэндлер будет срабатывать на кнопку 'Information about the bot developer' [button_100]
@router.message(Text(text='Information about the bot developer'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_en['developer'], reply_markup=keyboard_i_2_en)
