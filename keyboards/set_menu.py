from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


# Создаем объекты кнопок
button_1: KeyboardButton = KeyboardButton(text='Мой адрес')
button_2: KeyboardButton = KeyboardButton(text='Мой контактный телефон')
button_3: KeyboardButton = KeyboardButton(text='Показать фото маникюра')
button_4: KeyboardButton = KeyboardButton(text='Показать случайное фото маникюра')


# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[button_1, button_2],
                                                              [button_3],
                                                              [button_4]], resize_keyboard=True)
