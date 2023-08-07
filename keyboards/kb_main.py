from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import lexicon_button


# Создаем объекты кнопок 'Главное Меню'
button_6: KeyboardButton = KeyboardButton(text=lexicon_button['button_6'])
button_9: KeyboardButton = KeyboardButton(text=lexicon_button['button_9'])
button_8: KeyboardButton = KeyboardButton(text=lexicon_button['button_8'])
button_100: KeyboardButton = KeyboardButton(text=lexicon_button['button_100'])

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню'
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_6], [button_8], [button_9],
                                                              [button_100]],
                                                              resize_keyboard=True)

# Создаем объект инлайн-кнопки, ссылка на ТГ аккаунт Мой
url_button_2: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button['url_button_2'],
                                                          url='https://t.me/R1VaL24')

# Создаем объект инлайн-клавиатуры, ссылка на ТГ аккаунт Мой
keyboard_i_2: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[url_button_2]])
