from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon.lexicon_ru import lexicon_button


# Создаем объекты кнопок 'Меню Маникюр'
button_3: KeyboardButton = KeyboardButton(text=lexicon_button['button_3'])
button_4: KeyboardButton = KeyboardButton(text=lexicon_button['button_4'])
button_10: KeyboardButton = KeyboardButton(text=lexicon_button['button_10'])

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню'
keyboard_manicure: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_3], [button_4], [button_10]],
                                                             resize_keyboard=True)
