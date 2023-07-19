from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Мой адрес')
button_2: KeyboardButton = KeyboardButton(text='Мой контактный телефон')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]], resize_keyboard=True)
