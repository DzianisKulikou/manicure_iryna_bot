from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import lexicon_button


# Создаем объекты кнопок 'Главное Меню'
button_1: KeyboardButton = KeyboardButton(text=lexicon_button['button_1'])
button_2: KeyboardButton = KeyboardButton(text=lexicon_button['button_2'])
button_5: KeyboardButton = KeyboardButton(text=lexicon_button['button_5'])
button_6: KeyboardButton = KeyboardButton(text=lexicon_button['button_6'])

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню'
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_6], [button_1, button_2], [button_5]],
                                                              resize_keyboard=True)

# Создаем объект инлайн-кнопки, ссылка на ТГ аккаунт
url_button_1: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button['url_button_1'],
                                                          url='https://t.me/Ir1shka24')

# Создаем объект инлайн-клавиатуры
keyboard_i: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[url_button_1]])
