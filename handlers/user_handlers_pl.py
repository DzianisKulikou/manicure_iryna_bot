from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, FSInputFile

from database.database import users_db
from database.database_photo import photo_map, photo_certificates
from keyboards.kb_kontakt import keyboard_i_1_pl, keyboard_kontakt_pl
from keyboards.kb_main import keyboard_pl, keyboard_i_2_pl
from keyboards.keyboard_manicure import keyboard_manicure_pl
from keyboards.pagination_kb import create_pagination_kb_ser
from lexicon.lexicon_pl import lexicon_dict_pl, lexicon_certificates_pl

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на кнопку 'Mój adres' [button_1]
@router.message(Text(text='Mój adres'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_pl['adres'])
        await message.answer_photo(photo=FSInputFile(photo_map))


# Этот хэндлер будет срабатывать на кнопку 'Mój telefon kontaktowy' [button_2]
@router.message(Text(text='Mój telefon kontaktowy'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_pl['phone'])


# Этот хэндлер будет срабатывать на кнопку 'Cennik' [button_8]
@router.message(Text(text='Cennik'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_pl['price list'])


# Этот хэндлер будет срабатывать на кнопку 'Moje certyfikaty' [button_12]
@router.message(Text(text='Moje certyfikaty'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_certificates_pl['cer'])
        await message.answer(text=lexicon_certificates_pl['cer1'])
        index_photo = users_db[message.from_user.id]['page_certificates']
        await message.answer_photo(
            photo=FSInputFile(photo_certificates[index_photo]),
            reply_markup=create_pagination_kb_ser(
                'backward_cer',
                f'{users_db[message.from_user.id]["page_certificates"]}/{len(photo_certificates)}',
                'forward_cer'))


# Этот хэндлер будет срабатывать на кнопку 'Napisz do mnie w Telegramie' [button_5]
@router.message(Text(text='Napisz do mnie w Telegramie'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_pl['me'], reply_markup=keyboard_i_1_pl)


# Этот хэндлер будет срабатывать на кнопку 'Wszystkie informacje o pracy mistrza' [button_6]
@router.message(Text(text='Wszystkie informacje o pracy mistrza'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_pl['start_manicure'], reply_markup=keyboard_manicure_pl)


# Этот хэндлер будет срабатывать на кнопку 'Moje dane kontaktowe' [button_9]
@router.message(Text(text='Moje dane kontaktowe'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_pl['kontakt'], reply_markup=keyboard_kontakt_pl)


# Этот хэндлер будет срабатывать на кнопку 'Powrót do menu głównego' [button_10]
@router.message(Text(text='Powrót do menu głównego'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_pl['start_menu'], reply_markup=keyboard_pl)


# Этот хэндлер будет срабатывать на кнопку 'Informacje o twórcy bota' [button_100]
@router.message(Text(text='Informacje o twórcy bota'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_pl['developer'], reply_markup=keyboard_i_2_pl)
