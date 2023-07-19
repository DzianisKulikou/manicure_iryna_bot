from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandStart, Text
from lexicon.lexicon_ru import lexicon_dict_ru
from keyboards.set_menu import keyboard


# Инициализируем роутер уровня модуля
router: Router = Router()


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
    photo = FSInputFile('photo/maps/1.jpg')
    await message.answer_photo(photo=photo)


# Этот хэндлер будет срабатывать на кнопку 'Мой контактный телефон'
@router.message(Text(text='Мой контактный телефон'))
async def process_dog_answer(message: Message):
    await message.answer(text=lexicon_dict_ru['phone'])
