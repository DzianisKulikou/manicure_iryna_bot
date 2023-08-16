import asyncio
from random import randint

from aiogram import Router
from environs import Env
from aiogram.types import Message
from aiogram.filters import Text

from config_data.config import load_config
from lexicon.evidence import evidence

# Инициализируем роутер уровня модуля
router: Router = Router()

# Получаем id каналов бьюти и наша из .env
env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
config = load_config('.env')
CHANNEL_ID_NA = config.tg_bot.channel_id_na
CHANNEL_ID = config.tg_bot.channel_id


# для вывода в ЛС id чата
# await bot.send_message(message.from_user.id, message.chat.id)

# реклама в канал
@router.message(Text(text='реклама'))
async def process_dog_answer(message: Message, bot=None):
    print(message.chat.id)
    while True:
        await bot.send_message(chat_id=CHANNEL_ID_NA, text='Привет')
        await asyncio.sleep(86400)  # сутки


# Сообщения на канал 'Интересный факт'
@router.message(Text(text='интересный факт'))
async def process_dog_answer(message: Message, bot=None):
    print(message.chat.id)
    lst = []
    while True:
        key = randint(1, 10)
        if len(lst) == 6:
            lst = []
        elif key in lst:
            continue
        else:
            await bot.send_message(chat_id=CHANNEL_ID_NA, text=evidence[key])
            lst.append(key)
            await asyncio.sleep(10800)  # 3 часа
