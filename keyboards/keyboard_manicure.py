from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import lexicon_button, lexicon_button_in


# Создаем объекты кнопок 'Меню Маникюр'
button_3: KeyboardButton = KeyboardButton(text=lexicon_button['button_3'])
button_4: KeyboardButton = KeyboardButton(text=lexicon_button['button_4'])
button_7: KeyboardButton = KeyboardButton(text=lexicon_button['button_7'])
button_10: KeyboardButton = KeyboardButton(text=lexicon_button['button_10'])

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню'
keyboard_manicure: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_3], [button_4], [button_7], [button_10]],
                                                             resize_keyboard=True)

# Создаем объект инлайн-кнопки Дальше
button_in_1: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_in['button_in_1'],
                                                         callback_data='button_in_1')

# Создаем объект инлайн-клавиатуры
keyboard_in_1: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[button_in_1]])
