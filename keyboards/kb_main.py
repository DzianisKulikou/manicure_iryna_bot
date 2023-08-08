from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import lexicon_button, button_in_lg
from lexicon.lexicon_en import lexicon_button_en


# Создаем объекты кнопок 'Главное Меню' ru
_button_6: KeyboardButton = KeyboardButton(text=lexicon_button['button_6'])
_button_9: KeyboardButton = KeyboardButton(text=lexicon_button['button_9'])
_button_8: KeyboardButton = KeyboardButton(text=lexicon_button['button_8'])
_button_100: KeyboardButton = KeyboardButton(text=lexicon_button['button_100'])

# Создаем объекты кнопок 'Главное Меню' en
_button_6_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_6'])
_button_9_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_9'])
_button_8_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_8'])
_button_100_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_100'])

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню' ru
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_6], [_button_8], [_button_9],
                                                              [_button_100]],
                                                    resize_keyboard=True)

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню' en
keyboard_en: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_6_en], [_button_8_en], [_button_9_en],
                                                                 [_button_100_en]],
                                                       resize_keyboard=True)

# Создаем объект инлайн-кнопки, ссылка на ТГ аккаунт Мой ru
_url_button_2: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button['url_button_2'],
                                                           url='https://t.me/R1VaL24')

# Создаем объект инлайн-кнопки, ссылка на ТГ аккаунт Мой en
_url_button_2_en: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_en['url_button_2'],
                                                              url='https://t.me/R1VaL24')

# Создаем объект инлайн-клавиатуры, ссылка на ТГ аккаунт Мой ru
keyboard_i_2: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_url_button_2]])

# Создаем объект инлайн-клавиатуры, ссылка на ТГ аккаунт Мой en
keyboard_i_2_en: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_url_button_2_en]])

# Создаём объекты инлайн-кнопок выбора языков
button_in_lg1: InlineKeyboardButton = InlineKeyboardButton(text=button_in_lg['button_in_lg1'],
                                                           callback_data='button_in_lg1')
button_in_lg2: InlineKeyboardButton = InlineKeyboardButton(text=button_in_lg['button_in_lg2'],
                                                           callback_data='button_in_lg2')
button_in_lg3: InlineKeyboardButton = InlineKeyboardButton(text=button_in_lg['button_in_lg3'],
                                                           callback_data='button_in_lg3')

# Создаем объект инлайн-клавиатуры выбор языков
keyboard_in_lg: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_in_lg1, button_in_lg2,
                                                                             button_in_lg3]])