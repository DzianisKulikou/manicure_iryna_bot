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

# Правила нашего канала бьюти
@router.message(Text(text='правила'))
async def process_dog_answer(message: Message, bot=None):
    print(message.chat.id)
    while True:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text='<b>ЦЕЛЬ ГРУППЫ:</b>\nПоиск мастеров, моделей и клиентов в Варшаве из любой бьюти сферы!\n'
                 '<b>ПРАВИЛА ГРУППЫ:</b>\n\n<b>1)</b> В группе можно публиковать любые объявления, относящиеся к '
                 'бьюти сфере в Варшаве абсолютно бесплатно (поиск мастеров, поиск моделей, перечень предлагаемых '
                 'услуг и т.д.)!\n<b>2)</b> Дублировать одно и тоже объявление можно раз в сутки!\n<b>3)</b> '
                 'Объявление не должно нарушать законов РП!\n<b>4)</b> Языки общения на канале: 🇧🇾🇺🇦🇵🇱🇷🇺🇬🇧')
        await asyncio.sleep(172800)  # 2 суток


# Сообщения на канал 'Интересный факт'
@router.message(Text(text='интересный факт'))
async def process_dog_answer(message: Message, bot=None):
    print(message.chat.id)
    lst = []
    while True:
        key = randint(1, 100)
        if len(lst) == 60:
            lst = []
        elif key in lst:
            continue
        else:
            await bot.send_message(chat_id=CHANNEL_ID, text=evidence[key])
            lst.append(key)
            await asyncio.sleep(10800)  # 3 часа
