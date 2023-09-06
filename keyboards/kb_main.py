from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_pl import lexicon_button_pl
from lexicon.lexicon_ru import lexicon_button, button_in_lg
from lexicon.lexicon_en import lexicon_button_en


# Создаем объекты кнопок 'Главное Меню' ru
# Кнопка "Вся информация о работе мастера"
_button_6: KeyboardButton = KeyboardButton(text=lexicon_button['button_6'])
# Кнопка "Мои контактные данные"
_button_9: KeyboardButton = KeyboardButton(text=lexicon_button['button_9'])
# Кнопка "Прайс лист"
_button_8: KeyboardButton = KeyboardButton(text=lexicon_button['button_8'])
# Кнопка "Мои сертификаты"
_button_12: KeyboardButton = KeyboardButton(text=lexicon_button['button_12'])
# Кнопка "Лучший ТГ канал Beauty Warszawa"
_button_15: KeyboardButton = KeyboardButton(text=lexicon_button['button_15'])
# Кнопка "Информация о разработчике бота"
_button_100: KeyboardButton = KeyboardButton(text=lexicon_button['button_100'])

# Создаем объекты кнопок 'Главное Меню' en
# Кнопка "All information about the work of the wizard"
_button_6_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_6'])
# Кнопка "My contact details"
_button_9_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_9'])
# Кнопка "Price list"
_button_8_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_8'])
# Кнопка "My Certificates"
_button_12_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_12'])
# Кнопка "Best TG channel Beauty Warszawa"
_button_15_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_15'])
# Кнопка "Information about the bot developer"
_button_100_en: KeyboardButton = KeyboardButton(text=lexicon_button_en['button_100'])

# Создаем объекты кнопок 'Главное Меню' pl
# Кнопка "Wszystkie informacje o pracy mistrza"
_button_6_pl: KeyboardButton = KeyboardButton(text=lexicon_button_pl['button_6'])
# Кнопка "Moje dane kontaktowe"
_button_9_pl: KeyboardButton = KeyboardButton(text=lexicon_button_pl['button_9'])
# Кнопка "Cennik"
_button_8_pl: KeyboardButton = KeyboardButton(text=lexicon_button_pl['button_8'])
# Кнопка "Moje certyfikaty"
_button_12_pl: KeyboardButton = KeyboardButton(text=lexicon_button_pl['button_12'])
# Кнопка "Najlepszy kanał TG Beauty Warszawa"
_button_15_pl: KeyboardButton = KeyboardButton(text=lexicon_button_pl['button_15'])
# Кнопка "Informacje o twórcy bota"
_button_100_pl: KeyboardButton = KeyboardButton(text=lexicon_button_pl['button_100'])

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню' ru
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_6], [_button_8, _button_12],
                                                              [_button_9], [_button_15], [_button_100]],
                                                    resize_keyboard=True)

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню' en
keyboard_en: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_6_en], [_button_8_en, _button_12_en],
                                                                 [_button_9_en],[_button_15_en], [_button_100_en]],
                                                       resize_keyboard=True)

# Создаем объект клавиатуры, добавляя в него кнопки 'Главное Меню' pl
keyboard_pl: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[_button_6_pl], [_button_8_pl, _button_12_pl],
                                                                 [_button_9_pl], [_button_15_pl], [_button_100_pl]],
                                                       resize_keyboard=True)

# Создаем объект инлайн-кнопки, ссылка на ТГ аккаунт Мой ru
_url_button_2: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button['url_button_2'],
                                                           url='https://t.me/R1VaL24')

# Создаем объект инлайн-кнопки, ссылка на ТГ аккаунт Мой en
_url_button_2_en: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_en['url_button_2'],
                                                              url='https://t.me/R1VaL24')

# Создаем объект инлайн-кнопки, ссылка на ТГ аккаунт Мой pl
_url_button_2_pl: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_pl['url_button_2'],
                                                              url='https://t.me/R1VaL24')

# Создаем объект инлайн-клавиатуры, ссылка на ТГ аккаунт Мой ru
keyboard_i_2: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_url_button_2]])

# Создаем объект инлайн-клавиатуры, ссылка на ТГ аккаунт Мой en
keyboard_i_2_en: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_url_button_2_en]])

# Создаем объект инлайн-клавиатуры, ссылка на ТГ аккаунт Мой pl
keyboard_i_2_pl: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_url_button_2_pl]])

# Создаем объект инлайн-кнопки, ссылка на ТГ канал Beauty ru
_url_button_3: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button['url_button_3'],
                                                           url='https://t.me/beautywarsza')

# Создаем объект инлайн-кнопки, ссылка на ТГ канал Beauty en
_url_button_3_en: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_en['url_button_3'],
                                                              url='https://t.me/beautywarsza')

# Создаем объект инлайн-кнопки, ссылка на ТГ канал Beauty pl
_url_button_3_pl: InlineKeyboardButton = InlineKeyboardButton(text=lexicon_button_pl['url_button_3'],
                                                              url='https://t.me/beautywarsza')

# Создаем объект инлайн-клавиатуры, ссылка на ТГ канал Beauty ru
keyboard_i_3: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_url_button_3]])

# Создаем объект инлайн-клавиатуры, ссылка на ТГ канал Beauty en
keyboard_i_3_en: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_url_button_3_en]])

# Создаем объект инлайн-клавиатуры, ссылка на ТГ канал Beauty pl
keyboard_i_3_pl: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[_url_button_3_pl]])

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
