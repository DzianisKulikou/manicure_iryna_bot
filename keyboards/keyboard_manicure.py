from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import lexicon_button, lexicon_button_in
from lexicon.lexicon_en import lexicon_button_en, lexicon_button_in_en

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

# Создаем объект клавиатуры "Маникюр" ru
keyboard_manicure: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_11], [_button_7],
                                                                       [_button_10]],
                                                             resize_keyboard=True)

# Создаем объект клавиатуры "Маникюр" en
keyboard_manicure_en: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_11_en],
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

# Создаем объект инлайн-кнопки "Дальше" ru
_button_in_1: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_in['button_in_1'],
                                                          callback_data='button_in_1')

# Создаем объект инлайн-кнопки "Дальше" en
_button_in_1_en: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_in_en['button_in_1'],
                                                             callback_data='button_in_1_en')

# Создаем объект инлайн-клавиатуры с инлайн-кнопкой "Дальше" ru
keyboard_in_1: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_button_in_1]])

# Создаем объект инлайн-клавиатуры с инлайн-кнопкой "Дальше" en
keyboard_in_1_en: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_button_in_1_en]])
