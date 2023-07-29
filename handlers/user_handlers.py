from aiogram import Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Command, CommandStart, Text
from lexicon.lexicon_ru import lexicon_dict_ru, lexicon_disinfection
from keyboards.keyboard_utils import keyboard, keyboard_i
from keyboards.keyboard_manicure import keyboard_manicure, keyboard_in_1
from keyboards.pagination_kb import create_pagination_keyboard
from random import choice
from database.database import users_db, user_dict_template
from database.database_photo import photo_nails, photo_map, photo_disinfection
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
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['nails'])
        index_photo = users_db[message.from_user.id]['page']
        await message.answer_photo(photo=FSInputFile(photo_nails[index_photo]), reply_markup=create_pagination_keyboard(
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
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['photo_selection'])
        await message.answer_photo(photo=FSInputFile(choice(photo_nails)))


# Этот хэндлер будет срабатывать на кнопку 'Написать Ирине в Telegram'
@router.message(Text(text='Написать Ирине в Telegram'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['me'], reply_markup=keyboard_i)


# Этот хэндлер будет срабатывать на кнопку 'Вся информация о работе мастера'
@router.message(Text(text='Вся информация о работе мастера'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['start_manicure'], reply_markup=keyboard_manicure)


# Этот хэндлер будет срабатывать на кнопку 'Вернуться в главное меню' [button_10]
@router.message(Text(text='Вернуться в главное меню'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['start_menu'], reply_markup=keyboard)


# Этот хэндлер будет срабатывать на кнопку 'Дезинфекция и стерилизация инструмента' [button_7]
# @router.callback_query(Text(text='Дезинфекция и стерилизация инструмента'))
# async def process_dog_answer(callback: CallbackQuery):
#     await callback.message.answer(text=lexicon_disinfection['phrase1'])

    # await message.answer_photo(photo=FSInputFile(photo_disinfection[1]))
    # await message.answer(text=lexicon_disinfection['phrase2'])
    # await message.answer_photo(photo=FSInputFile(photo_disinfection[2]))
    # await message.answer_photo(photo=FSInputFile(photo_disinfection[3]))
    # await message.answer(text=lexicon_disinfection['phrase3'])
    # await message.answer_photo(photo=FSInputFile(photo_disinfection[4]))
    # await message.answer_photo(photo=FSInputFile(photo_disinfection[5]))


# Этот хэндлер будет срабатывать на кнопку 'Дезинфекция и стерилизация инструмента' [button_7]
@router.message(Text(text='Дезинфекция и стерилизация инструмента'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_disinfection['phrase1'], reply_markup=keyboard_in_1)

# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Далее"
# во время просмотра фотографий ногтей
@router.callback_query(Text(text='button_in_1'))
async def process_button_in_1(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page_disinfection'] < 21:
        users_db[callback.from_user.id]['page_disinfection'] += 1

        if users_db[callback.from_user.id]['page_disinfection'] == 2:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[1]), reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 3:
            await callback.message.answer(text=lexicon_disinfection['phrase2'], reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 4:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[2]), reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 5:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[3]), reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 6:
            await callback.message.answer(text=lexicon_disinfection['phrase3'], reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 7:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[4]), reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 8:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[5]), reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 9:
            await callback.message.answer(text=lexicon_disinfection['phrase4'], reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 10:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[6]), reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 11:
            await callback.message.answer(text=lexicon_disinfection['phrase5'], reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 12:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[7]), reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 13:
            await callback.message.answer(text=lexicon_disinfection['phrase6'], reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 14:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[8]), reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 15:
            await callback.message.answer(text=lexicon_disinfection['phrase7'], reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 16:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[9]), reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 17:
            await callback.message.answer(text=lexicon_disinfection['phrase8'], reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 18:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[10]), reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 19:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[11]), reply_markup=keyboard_in_1)
        if users_db[callback.from_user.id]['page_disinfection'] == 20:
            await callback.message.answer(text=lexicon_disinfection['phrase9'])
            users_db[callback.from_user.id]['page_disinfection'] = 1

    await callback.answer()
