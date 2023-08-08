from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import lexicon_button
from lexicon.lexicon_en import lexicon_button_en

# Создаем объекты кнопок 'Мои контактные данные' ru
_button_1: KeyboardButton = KeyboardButton(text=lexicon_button['button_1'])
_button_2: KeyboardButton = KeyboardButton(text=lexicon_button['button_2'])
_button_5: KeyboardButton = KeyboardButton(text=lexicon_button['button_5'])
_button_10: KeyboardButton = KeyboardButton(text=lexicon_button['button_10'])

# Создаем объекты кнопок 'Мои контактные данные' en
_button_1_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_1'])
_button_2_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_2'])
_button_5_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_5'])
_button_10_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_10'])

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню' ru
keyboard_kontakt: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_1, _button_2], [_button_5],
                                                                      [_button_10]],
                                                            resize_keyboard=True)

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню' en
keyboard_kontakt_en: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_1_en, _button_2_en], [_button_5_en],
                                                                         [_button_10_en]],
                                                               resize_keyboard=True)

# Создаем объект инлайн-кнопки, ссылка на ТГ аккаунт Иры ru
_url_button_1: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button['url_button_1'],
                                                           url='https://t.me/Ir1shka24')

# Создаем объект инлайн-кнопки, ссылка на ТГ аккаунт Иры en
_url_button_1_en: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_en['url_button_1'],
                                                              url='https://t.me/Ir1shka24')

# Создаем объект инлайн-клавиатуры, ссылка на ТГ аккаунт Иры ru
keyboard_i_1: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_url_button_1]])

# Создаем объект инлайн-клавиатуры, ссылка на ТГ аккаунт Иры en
keyboard_i_1_en: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_url_button_1_en]])
