from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import lexicon_button, lexicon_button_in, lexicon_b_in_gel_back
from lexicon.lexicon_en import lexicon_button_en, lexicon_button_in_en, lexicon_b_in_gel_back_en

# Создаем объекты кнопок 'Меню Маникюр' ru
# Кнопка "Фотографии маникюра"
_button_3: KeyboardButton = KeyboardButton(text=lexicon_button['button_3'])
# Кнопка "Случайная фотография маникюра"
_button_4: KeyboardButton = KeyboardButton(text=lexicon_button['button_4'])
# Кнопка "Дезинфекция и стерилизация инструмента"
_button_7: KeyboardButton = KeyboardButton(text=lexicon_button['button_7'])
# Кнопка "Вернуться в главное меню"
_button_10: KeyboardButton = KeyboardButton(text=lexicon_button['button_10'])
# Кнопка "Фотографии моих работ"
_button_11: KeyboardButton = KeyboardButton(text=lexicon_button['button_11'])
# Кнопка "Аппараты"
_button_13: KeyboardButton = KeyboardButton(text=lexicon_button['button_13'])
# Кнопка "Гель-лаки"
_button_14: KeyboardButton = KeyboardButton(text=lexicon_button['button_14'])

# Создаем объекты кнопок 'Меню Маникюр' en
# Кнопка "Manicure Photos"
_button_3_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_3'])
# Кнопка "Random manicure photo"
_button_4_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_4'])
# Кнопка "Disinfection and sterilization of the instrument"
_button_7_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_7'])
# Кнопка "Go back to the main menu"
_button_10_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_10'])
# Кнопка "Photos of my works"
_button_11_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_11'])
# Кнопка "Devices"
_button_13_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_13'])
# Кнопка "Gel-polishes"
_button_14_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_14'])

# Создаем объект клавиатуры "Маникюр" ru
keyboard_manicure: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_11], [_button_13, _button_14],
                                                                       [_button_7], [_button_10]],
                                                             resize_keyboard=True)

# Создаем объект клавиатуры "Маникюр" en
keyboard_manicure_en: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_11_en],
                                                                          [_button_13_en, _button_14_en],
                                                                          [_button_7_en], [_button_10_en]],
                                                                resize_keyboard=True)

# Создаем объект клавиатуры "Фото работ" ru
kb_manicure_photo: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_3], [_button_4],
                                                                       [_button_10]],
                                                             resize_keyboard=True)

# Создаем объект клавиатуры "Фото работ" en
kb_manicure_photo_en: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_3_en],
                                                                          [_button_4_en], [_button_10_en]],
                                                                resize_keyboard=True)

# Создаем объект инлайн-кнопки "Дальше >>" ru
_button_in_2: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_in['button_in_2'],
                                                          callback_data='button_in_2')

# Создаем объект инлайн-кнопки "Further >>" en
_button_in_2_en: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_in_en['button_in_2'],
                                                             callback_data='button_in_2_en')

# Создаем объект инлайн-клавиатуры с инлайн-кнопкой "Дальше >>" ru
keyboard_in_2: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_button_in_2]])

# Создаем объект инлайн-клавиатуры с инлайн-кнопкой "Further >>" en
keyboard_in_2_en: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_button_in_2_en]])

# Создаем объект инлайн-кнопки "Дальше" ru
_button_in_1: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_in['button_in_1'],
                                                          callback_data='button_in_1')

# Создаем объект инлайн-кнопки "Further" en
_button_in_1_en: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_in_en['button_in_1'],
                                                             callback_data='button_in_1_en')

# Создаем объект инлайн-клавиатуры с инлайн-кнопкой "Дальше" ru
keyboard_in_1: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_button_in_1]])

# Создаем объект инлайн-клавиатуры с инлайн-кнопкой "Дальше" en
keyboard_in_1_en: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_button_in_1_en]])

# Создаём объект инлайн-кнопок "Для лаков" ru en pl
_b_in_gel_1: InlineKeyboardButton = InlineKeyboardButton(text='1', callback_data='_b_in_gel_1')
_b_in_gel_2: InlineKeyboardButton = InlineKeyboardButton(text='2', callback_data='_b_in_gel_2')
_b_in_gel_3: InlineKeyboardButton = InlineKeyboardButton(text='3', callback_data='_b_in_gel_3')
_b_in_gel_4: InlineKeyboardButton = InlineKeyboardButton(text='4', callback_data='_b_in_gel_4')
_b_in_gel_5: InlineKeyboardButton = InlineKeyboardButton(text='5', callback_data='_b_in_gel_5')
_b_in_gel_6: InlineKeyboardButton = InlineKeyboardButton(text='6', callback_data='_b_in_gel_6')
_b_in_gel_7: InlineKeyboardButton = InlineKeyboardButton(text='7', callback_data='_b_in_gel_7')
_b_in_gel_8: InlineKeyboardButton = InlineKeyboardButton(text='8', callback_data='_b_in_gel_8')
_b_in_gel_9: InlineKeyboardButton = InlineKeyboardButton(text='9', callback_data='_b_in_gel_9')
_b_in_gel_10: InlineKeyboardButton = InlineKeyboardButton(text='10', callback_data='_b_in_gel_10')
_b_in_gel_11: InlineKeyboardButton = InlineKeyboardButton(text='11', callback_data='_b_in_gel_11')
_b_in_gel_12: InlineKeyboardButton = InlineKeyboardButton(text='12', callback_data='_b_in_gel_12')
_b_in_gel_13: InlineKeyboardButton = InlineKeyboardButton(text='13', callback_data='_b_in_gel_13')
_b_in_gel_14: InlineKeyboardButton = InlineKeyboardButton(text='14', callback_data='_b_in_gel_14')
_b_in_gel_15: InlineKeyboardButton = InlineKeyboardButton(text='15', callback_data='_b_in_gel_15')

# Создаем объект инлайн-клавиатуры с инлайн-кнопками "Для лаков" ru en pl
kb_in_gel: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[_b_in_gel_1, _b_in_gel_2, _b_in_gel_3, _b_in_gel_4,
                      _b_in_gel_5, _b_in_gel_6, _b_in_gel_7, _b_in_gel_8],
                     [_b_in_gel_9, _b_in_gel_10, _b_in_gel_11, _b_in_gel_12,
                      _b_in_gel_13, _b_in_gel_14, _b_in_gel_15]])

# Создаём объект инлайн-кнопки "Для лаков" возврат ru
_b_in_gel_back: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_b_in_gel_back['_b_in_gel_back'],
                                                            callback_data='_b_in_gel_back')

# Создаём объект инлайн-кнопки "Для лаков возврат" en
_b_in_gel_back_en: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_b_in_gel_back_en['_b_in_gel_back'],
                                                            callback_data='_b_in_gel_back_en')

# Создаем объект инлайн-клавиатуры с инлайн-кнопкой "Для лаков возврат" ru
kb_in_gel_back: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_b_in_gel_back]])

# Создаем объект инлайн-клавиатуры с инлайн-кнопкой "Для лаков возврат" en
kb_in_gel_back_en: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_b_in_gel_back_en]])
