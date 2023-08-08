from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import lexicon_button, lexicon_button_in
from lexicon.lexicon_en import lexicon_button_en, lexicon_button_in_en

# Создаем объекты кнопок 'Меню Маникюр' ru
_button_3: KeyboardButton = KeyboardButton(text=lexicon_button['button_3'])
_button_4: KeyboardButton = KeyboardButton(text=lexicon_button['button_4'])
_button_7: KeyboardButton = KeyboardButton(text=lexicon_button['button_7'])
_button_10: KeyboardButton = KeyboardButton(text=lexicon_button['button_10'])

# Создаем объекты кнопок 'Меню Маникюр' en
_button_3_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_3'])
_button_4_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_4'])
_button_7_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_7'])
_button_10_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_10'])

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню' ru
keyboard_manicure: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_3], [_button_4], [_button_7],
                                                                       [_button_10]],
                                                             resize_keyboard=True)

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню' en
keyboard_manicure_en: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_3_en], [_button_4_en],
                                                                          [_button_7_en], [_button_10_en]],
                                                                resize_keyboard=True)

# Создаем объект инлайн-кнопки Дальше ru
_button_in_1: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_in['button_in_1'],
                                                          callback_data='button_in_1')

# Создаем объект инлайн-кнопки Дальше en
_button_in_1_en: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_in_en['button_in_1'],
                                                             callback_data='button_in_1_en')

# Создаем объект инлайн-клавиатуры ru
keyboard_in_1: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_button_in_1]])

# Создаем объект инлайн-клавиатуры en
keyboard_in_1_en: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_button_in_1_en]])
