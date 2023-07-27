from aiogram import Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command, CommandStart, Text
from lexicon.lexicon_ru import lexicon_dict_ru
from keyboards.keyboard_utils import keyboard, keyboard_i
from keyboards.keyboard_manicure import keyboard_manicure
from keyboards.pagination_kb import create_pagination_keyboard
from random import choice
from database.database import users_db, user_dict_template
from database.database_photo import photo_nails, photo_map
from copy import deepcopy

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=lexicon_dict_ru['/start'])
    await message.answer(text=lexicon_dict_ru['menu'], reply_markup=keyboard)
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)


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


# Этот хэндлер будет срабатывать на кнопку 'База фотографий моих работ маникюра' новое сообщение с фото
# @router.message(Text(text='База фотографий моих работ маникюра'))
# async def process_dog_answer(message: Message):
#     await message.answer(text=lexicon_dict_ru['nails'])
#     for i in photo_nails:
#         photo = FSInputFile(i)
#         await message.answer_photo(photo=photo)


# Этот хэндлер будет срабатывать на кнопку 'База фотографий моих работ маникюра' с удалением старого фото
@router.message(Text(text='База фотографий моих работ маникюра'))
async def process_dog_answer(message: Message):
    await message.answer(text=lexicon_dict_ru['nails'])
    index_photo = users_db[message.from_user.id]['page']
    photo = FSInputFile(photo_nails[index_photo])
    await message.answer_photo(photo=photo, reply_markup=create_pagination_keyboard(
        'backward',
        f'{users_db[message.from_user.id]["page"]}/{len(photo_nails)}',
        'forward'))


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "вперед"
# во время просмотра фотографий ногтей
@router.callback_query(Text(text='forward'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] < len(photo_nails):
        users_db[callback.from_user.id]['page'] += 1
        index_photo = users_db[callback.from_user.id]['page']
        photo = FSInputFile(photo_nails[index_photo])
        await callback.message.answer_photo(photo=photo,
                                            reply_markup=create_pagination_keyboard(
                                                'backward',
                                                f'{users_db[callback.from_user.id]["page"]}/{len(photo_nails)}',
                                                'forward'))
        # Удаляем сообщение, в котором была нажата кнопка
        await callback.message.delete()
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "назад"
# во время просмотра фотографий ногтей
@router.callback_query(Text(text='backward'))
async def process_forward_press(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page'] > 1:
        users_db[callback.from_user.id]['page'] -= 1
        index_photo = users_db[callback.from_user.id]['page']
        photo = FSInputFile(photo_nails[index_photo])
        await callback.message.answer_photo(photo=photo,
                                            reply_markup=create_pagination_keyboard(
                                                'backward',
                                                f'{users_db[callback.from_user.id]["page"]}/{len(photo_nails)}',
                                                'forward'))
        # Удаляем сообщение, в котором была нажата кнопка
        await callback.message.delete()
    await callback.answer()


# Этот хэндлер будет срабатывать на кнопку 'Показать случайную фотографию моего маникюра'
@router.message(Text(text='Показать случайную фотографию моего маникюра'))
async def process_dog_answer(message: Message):
    await message.answer(text=lexicon_dict_ru['photo_selection'])
    photo = FSInputFile(choice(photo_nails))
    await message.answer_photo(photo=photo)


# Этот хэндлер будет срабатывать на кнопку 'Написать Ирине в Telegram'
@router.message(Text(text='Написать Ирине в Telegram'))
async def process_dog_answer(message: Message):
    await message.answer(text=lexicon_dict_ru['me'], reply_markup=keyboard_i)


# Этот хэндлер будет срабатывать на кнопку 'Вся информация о работе мастера'
@router.message(Text(text='Вся информация о работе мастера'))
async def process_dog_answer(message: Message):
    await message.answer(text=lexicon_dict_ru['start_manicure'], reply_markup=keyboard_manicure)


# Этот хэндлер будет срабатывать на кнопку 'Вернуться в главное меню'
@router.message(Text(text='Вернуться в главное меню'))
async def process_dog_answer(message: Message):
    await message.answer(text=lexicon_dict_ru['start_menu'], reply_markup=keyboard)
