from random import randint

from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, FSInputFile, CallbackQuery

from database.database import users_db
from database.database_photo import photo_nails, photo_disinfection, photo_devices, photo_gel_polishes
from filters.filters import IsBase
from keyboards.keyboard_manicure import kb_manicure_photo_en, keyboard_in_1_en, keyboard_in_2_en, kb_in_gel
from keyboards.pagination_kb import create_pagination_keyboard
from lexicon.lexicon_en import lexicon_dict_en, lexicon_disinfection_en, lexicon_devices_en, lexicon_gel_polishes_en

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер будет срабатывать на кнопку 'Photos of my works' [button_11]
@router.message(Text(text='Photos of my works'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_en['manicure_photo'], reply_markup=kb_manicure_photo_en)


# Этот хэндлер будет срабатывать на кнопку 'Manicure Photos' с удалением старого фото [button_3]
@router.message(Text(text='Manicure Photos'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_en['nails'])
        index_photo = users_db[message.from_user.id]['page']
        await message.answer_photo(photo=FSInputFile(photo_nails[index_photo]), reply_markup=create_pagination_keyboard(
            'backward',
            f'{users_db[message.from_user.id]["page"]}/{len(photo_nails)}',
            'forward'))


# Этот хэндлер будет срабатывать на кнопку 'Random manicure photo' [button_4]
@router.message(Text(text='Random manicure photo'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_dict_en['photo_selection'])
        await message.answer_photo(photo=FSInputFile(photo_nails[randint(1, 36)]))  # Список фото


# Этот хэндлер будет срабатывать на кнопку 'Devices' [button_13]
@router.message(Text(text='Devices'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_devices_en['devices1'], reply_markup=keyboard_in_2_en)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Дальше >>" для раздела Аппараты
@router.callback_query(Text(text='button_in_2_en'), IsBase(users_db))
async def process_button_in_1(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page_devices'] < 6:
        users_db[callback.from_user.id]['page_devices'] += 1

        if users_db[callback.from_user.id]['page_devices'] == 2:
            await callback.message.answer_photo(photo=FSInputFile(photo_devices[1]), reply_markup=keyboard_in_2_en)
        if users_db[callback.from_user.id]['page_devices'] == 3:
            await callback.message.answer(text=lexicon_devices_en['devices2'], reply_markup=keyboard_in_2_en)
        if users_db[callback.from_user.id]['page_devices'] == 4:
            await callback.message.answer_photo(photo=FSInputFile(photo_devices[2]), reply_markup=keyboard_in_2_en)
        if users_db[callback.from_user.id]['page_devices'] == 5:
            await callback.message.answer(text=lexicon_devices_en['devices3'])
            users_db[callback.from_user.id]['page_devices'] = 1

    await callback.answer()


# Этот хэндлер будет срабатывать на кнопку 'Disinfection and sterilization of the instrument' [button_7]
@router.message(Text(text='Disinfection and sterilization of the instrument'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_disinfection_en['phrase1'], reply_markup=keyboard_in_1_en)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки "Further"
@router.callback_query(Text(text='button_in_1_en'), IsBase(users_db))
async def process_button_in_1(callback: CallbackQuery):
    if users_db[callback.from_user.id]['page_disinfection'] < 21:
        users_db[callback.from_user.id]['page_disinfection'] += 1

        if users_db[callback.from_user.id]['page_disinfection'] == 2:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[1]), reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 3:
            await callback.message.answer(text=lexicon_disinfection_en['phrase2'], reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 4:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[2]), reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 5:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[3]), reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 6:
            await callback.message.answer(text=lexicon_disinfection_en['phrase3'], reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 7:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[4]), reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 8:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[5]), reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 9:
            await callback.message.answer(text=lexicon_disinfection_en['phrase4'], reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 10:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[6]), reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 11:
            await callback.message.answer(text=lexicon_disinfection_en['phrase5'], reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 12:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[7]), reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 13:
            await callback.message.answer(text=lexicon_disinfection_en['phrase6'], reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 14:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[8]), reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 15:
            await callback.message.answer(text=lexicon_disinfection_en['phrase7'], reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 16:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[9]), reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 17:
            await callback.message.answer(text=lexicon_disinfection_en['phrase8'], reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 18:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[10]),
                                                reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 19:
            await callback.message.answer_photo(photo=FSInputFile(photo_disinfection[11]),
                                                reply_markup=keyboard_in_1_en)
        if users_db[callback.from_user.id]['page_disinfection'] == 20:
            await callback.message.answer(text=lexicon_disinfection_en['phrase9'])
            users_db[callback.from_user.id]['page_disinfection'] = 1

    await callback.answer()


# Этот хэндлер будет срабатывать на кнопку 'Gel-polishes' [button_14]
@router.message(Text(text='Gel-polishes'), IsBase(users_db))
async def process_dog_answer(message: Message):
    if message.from_user.id == message.chat.id:
        await message.answer(text=lexicon_gel_polishes_en['gel_polishes1'])
        await message.answer_photo(photo=FSInputFile(photo_gel_polishes[0]), reply_markup=kb_in_gel)


# Этот хэндлер будет срабатывать на инлайн-кнопку '_b_in_gel_back_en' [_b_in_gel_back_en]
@router.callback_query(Text(text='_b_in_gel_back_en'), IsBase(users_db))
async def process_button_in_1(callback: CallbackQuery):
    await callback.message.answer_photo(photo=FSInputFile(photo_gel_polishes[0]), reply_markup=kb_in_gel)
