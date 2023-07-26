from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup)
from lexicon.lexicon_ru import lexicon_button


# Создаем объекты кнопок 'Главное Меню'
button_1: KeyboardButton = KeyboardButton(text=lexicon_button['button_1'])
button_2: KeyboardButton = KeyboardButton(text=lexicon_button['button_2'])
button_3: KeyboardButton = KeyboardButton(text=lexicon_button['button_3'])
button_4: KeyboardButton = KeyboardButton(text=lexicon_button['button_4'])
button_5: KeyboardButton = KeyboardButton(text=lexicon_button['button_5'])

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню'
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2],
                                                              [button_3],
                                                              [button_4],
                                                              [button_5]], resize_keyboard=True)

# Создаем объекты инлайн-кнопок
url_button_1: InlineKeyboardButton = InlineKeyboardButton(
                                    text=lexicon_button['url_button_1'],
                                    url='https://t.me/Ir1shka24')

# Создаем объект инлайн-клавиатуры
keyboard_i: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1]])
