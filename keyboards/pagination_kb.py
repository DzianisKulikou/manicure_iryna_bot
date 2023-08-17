from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon_ru import lexicon_pagination_kb, lexicon_pagination_kb_cer


# Функция, генерирующая клавиатуру для листания страниц работ ногтей
def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(*[InlineKeyboardButton(
        text=lexicon_pagination_kb[button] if button in lexicon_pagination_kb else button,
        callback_data=button) for button in buttons])
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Функция, генерирующая клавиатуру для листания страниц работ ногтей
def create_pagination_kb_ser(*buttons: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(*[InlineKeyboardButton(
        text=lexicon_pagination_kb_cer[button] if button in lexicon_pagination_kb_cer else button,
        callback_data=button) for button in buttons])
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()
