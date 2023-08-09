from aiogram import Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Text
from lexicon.lexicon_ru import lexicon_dict_ru, lexicon_disinfection
from keyboards.keyboard_manicure import keyboard_in_1
from keyboards.pagination_kb import create_pagination_keyboard
from random import randint
from database.database import users_db
from database.database_photo import photo_nails, photo_disinfection


# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на кнопку 'База фотографий моих работ маникюра' новое сообщение с фото
# @router.message(Text(text='База фотографий моих работ маникюра'))
# async def process_dog_answer(message: Message):
#     await message.answer(text=lexicon_dict_ru['nails'])
#     for i in photo_nails:
#         photo = FSInputFile(i)
#         await message.answer_photo(photo=photo)


# Этот хэндлер будет срабатывать на кнопку 'Фотографии маникюра' с удалением старого фото [button_3]
@router.message(Text(text='Фотографии маникюра'))
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


# Этот хэндлер будет срабатывать на кнопку 'Случайная фотография маникюра' [button_4]
@router.message(Text(text='Случайная фотография маникюра'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['photo_selection'])
        await message.answer_photo(photo=FSInputFile(photo_nails[randint(1, 24)]))  # Список фото


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
