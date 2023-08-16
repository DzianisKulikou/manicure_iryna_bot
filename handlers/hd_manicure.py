from aiogram import Router
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.filters import Text
from lexicon.lexicon_ru import lexicon_dict_ru, lexicon_disinfection, lexicon_devices, lexicon_gel_polishes
from keyboards.keyboard_manicure import *
from keyboards.pagination_kb import create_pagination_keyboard
from random import randint
from database.database import users_db
from database.database_photo import photo_nails, photo_disinfection, photo_devices, photo_gel_polishes

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на кнопку 'Фотографии моих работ' [button_11]
@router.message(Text(text='Фотографии моих работ'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_ru['manicure_photo'], reply_markup=kb_manicure_photo)


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


# Этот хэндлер будет срабатывать на кнопку 'Аппараты' [button_13]
@router.message(Text(text='Аппараты'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_devices['devices1'], reply_markup=keyboard_in_2)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Дальше >>" для раздела Аппараты
@router.callback_query(Text(text='button_in_2'))
async def process_button_in_1(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page_devices'] < 6:
        users_db[callback.from_user.id]['page_devices'] += 1

        if users_db[callback.from_user.id]['page_devices'] == 2:
            await callback.message.answer_photo(photo=FSInputFile(photo_devices[1]), reply_markup=keyboard_in_2)
        if users_db[callback.from_user.id]['page_devices'] == 3:
            await callback.message.answer(text=lexicon_devices['devices2'], reply_markup=keyboard_in_2)
        if users_db[callback.from_user.id]['page_devices'] == 4:
            await callback.message.answer_photo(photo=FSInputFile(photo_devices[2]), reply_markup=keyboard_in_2)
        if users_db[callback.from_user.id]['page_devices'] == 5:
            await callback.message.answer(text=lexicon_devices['devices3'])
            users_db[callback.from_user.id]['page_devices'] = 1

    await callback.answer()


# Этот хэндлер будет срабатывать на кнопку 'Дезинфекция и стерилизация инструмента' [button_7]
@router.message(Text(text='Дезинфекция и стерилизация инструмента'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_disinfection['phrase1'], reply_markup=keyboard_in_1)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Далее" для раздела Дезинфекция
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


# Этот хэндлер будет срабатывать на кнопку 'Гель-лаки' [button_14]
@router.message(Text(text='Гель-лаки'))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_gel_polishes['gel_polishes1'])
        await message.answer_photo(photo=FSInputFile(photo_gel_polishes[0]), reply_markup=kb_in_gel)


# Этот хэндлер будет срабатывать на инлайн-кнопку '1' [_b_in_gel_1]
@router.callback_query(Text(text='_b_in_gel_1'))
async def process_b_in_gel_1(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[1]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[1]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '2' [_b_in_gel_2]
@router.callback_query(Text(text='_b_in_gel_2'))
async def process_b_in_gel_2(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[2]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[2]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '3' [_b_in_gel_3]
@router.callback_query(Text(text='_b_in_gel_3'))
async def process_b_in_gel_3(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[3]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[3]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '4' [_b_in_gel_4]
@router.callback_query(Text(text='_b_in_gel_4'))
async def process_b_in_gel_4(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[4]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[4]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '5' [_b_in_gel_5]
@router.callback_query(Text(text='_b_in_gel_5'))
async def process_b_in_gel_5(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[5]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[5]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '6' [_b_in_gel_6]
@router.callback_query(Text(text='_b_in_gel_6'))
async def process_b_in_gel_6(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[6]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[6]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '7' [_b_in_gel_7]
@router.callback_query(Text(text='_b_in_gel_7'))
async def process_b_in_gel_7(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[7]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[7]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '8' [_b_in_gel_8]
@router.callback_query(Text(text='_b_in_gel_8'))
async def process_b_in_gel_8(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[8]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[8]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '9' [_b_in_gel_9]
@router.callback_query(Text(text='_b_in_gel_9'))
async def process_b_in_gel_9(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[9]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[9]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '10' [_b_in_gel_10]
@router.callback_query(Text(text='_b_in_gel_10'))
async def process_b_in_gel_10(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[10]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[10]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '11' [_b_in_gel_11]
@router.callback_query(Text(text='_b_in_gel_11'))
async def process_b_in_gel_11(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[11]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[11]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '12' [_b_in_gel_12]
@router.callback_query(Text(text='_b_in_gel_12'))
async def process_b_in_gel_12(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[12]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[12]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '13' [_b_in_gel_13]
@router.callback_query(Text(text='_b_in_gel_13'))
async def process_b_in_gel_13(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[13]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[13]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '14' [_b_in_gel_14]
@router.callback_query(Text(text='_b_in_gel_14'))
async def process_b_in_gel_14(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[14]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[14]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '15' [_b_in_gel_15]
@router.callback_query(Text(text='_b_in_gel_15'))
async def process_b_in_gel_15(callback: CallbackQuery):
    if users_db[callback.from_user.id]['language'] == 'ru':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[15]), reply_markup=kb_in_gel_back)
    elif users_db[callback.from_user.id]['language'] == 'en':
        await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[15]), reply_markup=kb_in_gel_back_en)


# Этот хэндлер будет срабатывать на инлайн-кнопку '_b_in_gel_back' [_b_in_gel_back]
@router.callback_query(Text(text='_b_in_gel_back'))
async def process_button_in_1(callback: CallbackQuery):
    await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[0]), reply_markup=kb_in_gel)
