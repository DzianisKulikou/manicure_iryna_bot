from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon_ru import lexicon_button


# Создаем объекты кнопок 'Мои контактные данные'
button_1: KeyboardButton = KeyboardButton(text=lexicon_button['button_1'])
button_2: KeyboardButton = KeyboardButton(text=lexicon_button['button_2'])
button_5: KeyboardButton = KeyboardButton(text=lexicon_button['button_5'])
button_10: KeyboardButton = KeyboardButton(text=lexicon_button['button_10'])

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню'
keyboard_kontakt: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2], [button_5],
                                                              [button_10]],
                                                              resize_keyboard=True)
