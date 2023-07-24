from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandStart, Text
from lexicon.lexicon_ru import lexicon_dict_ru
from keyboards.keyboard_utils import keyboard
from random import choice


# Инициализируем роутер уровня модуля
router: Router = Router()

# Фотографии ногтей
photo_nails = ['photo/nails/101.jpg', 'photo/nails/102.jpg', 'photo/nails/103.jpg', 'photo/nails/104.jpg',
               'photo/nails/105.jpg', 'photo/nails/106.jpg', 'photo/nails/107.jpg', 'photo/nails/108.jpg',
               'photo/nails/109.jpg', 'photo/nails/110.jpg', 'photo/nails/111.jpg', 'photo/nails/112.jpg']

photo_map = 'photo/maps/1.jpg'


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=lexicon_dict_ru['/start'])
    await message.answer(text=lexicon_dict_ru['menu'], reply_markup=keyboard)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=lexicon_dict_ru['/help'])


# Этот хэндлер будет срабатывать на кнопку 'Мой адрес'
@router.message(Text(text='Мой адрес'))
async def process_dog_answer(message: Message):
    await message.answer(text=lexicon_dict_ru['adres'])
    photo = FSInputFile(photo_map)
    await message.answer_photo(photo=photo)


# Этот хэндлер будет срабатывать на кнопку 'Мой контактный телефон'
@router.message(Text(text='Мой контактный телефон'))
async def process_dog_answer(message: Message):
    await message.answer(text=lexicon_dict_ru['phone'])


# Этот хэндлер будет срабатывать на кнопку 'Мой контактный телефон'
@router.message(Text(text='Показать фото маникюра'))
async def process_dog_answer(message: Message):
    await message.answer(text=lexicon_dict_ru['nails'])
    for i in photo_nails:
        photo = FSInputFile(i)
        await message.answer_photo(photo=photo)


# Этот хэндлер будет срабатывать на кнопку 'Мой контактный телефон'
@router.message(Text(text='Показать случайное фото маникюра'))
async def process_dog_answer(message: Message):
    photo = FSInputFile(choice(photo_nails))
    await message.answer_photo(photo=photo)
