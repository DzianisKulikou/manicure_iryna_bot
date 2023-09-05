import asyncio
from random import randint

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State, default_state
from environs import Env
from aiogram.types import Message, FSInputFile
from aiogram.filters import Text, StateFilter

from config_data.config import load_config
from database.database_photo import photo_nails
from lexicon.evidence import evidence

# Инициализируем роутер уровня модуля
router: Router = Router()

# Получаем данные из .env
env = Env()  # Создаем экземпляр класса Env
env.read_env()  # Методом read_env() читаем файл .env и загружаем из него переменные в окружение
config = load_config('.env')
CHANNEL_ID_NA = config.tg_bot.channel_id_na
CHANNEL_ID = config.tg_bot.channel_id
ADMIN_ID = config.tg_bot.admin_id

# для вывода в ЛС id чата
# await bot.send_message(message.from_user.id, message.chat.id)


# Правила нашего канала бьюти
@router.message(Text(text='правила'))
async def process_dog_answer(message: Message, bot=None):
    if str(message.from_user.id) in ADMIN_ID:
        print(message.chat.id)
        while True:
            await bot.send_message(
                chat_id=CHANNEL_ID,
                text='<b>ЦЕЛЬ ГРУППЫ:</b>\nПоиск мастеров, моделей и клиентов в Варшаве из любой бьюти сферы!\n\n'
                     '<b>ПРАВИЛА ГРУППЫ:</b>\n<b>1)</b> В группе можно публиковать любые объявления, относящиеся к '
                     'бьюти сфере в Варшаве абсолютно бесплатно (поиск мастеров, поиск моделей, перечень предлагаемых '
                     'услуг и т.д.)!\n<b>2)</b> Дублировать одно и тоже объявление можно раз в сутки!\n<b>3)</b> '
                     'Объявление не должно нарушать законов РП!\n<b>4)</b> Языки общения на канале: 🇧🇾🇺🇦🇵🇱🇷🇺🇬🇧\n'
                     '<b>5)</b> Если вы хотите публиковать в группе объявления, которые не относятся к бьюти сфере, '
                     'необходимо согласовать с администратором группы https://t.me/R1VaL24.\n\nВсе объявления '
                     'нарушающие правила группы будут удалены. Если вы дублируете одно и тоже объявление чаще чем '
                     'раз в сутки, удалите своё предыдущее объявление, в противном случае возможна блокировка вас '
                     'на канале!')
            await asyncio.sleep(172800)  # 2 суток


# Сообщения на канал бьюти 'Интересный факт'
@router.message(Text(text='интересный факт'))
async def process_dog_answer(message: Message, bot=None):
    if str(message.from_user.id) in ADMIN_ID:
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


# Объявление Иры на канал бьюти
# создаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSMFillForm(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодействия с пользователем
    fill_dates = State()        # Состояние ожидания ввода имени


# Этот хэндлер будет срабатывать на команду "объявление"
# и переводить бота в состояние ожидания ввода дат
@router.message(Text(text='объявление'), StateFilter(default_state))
async def process_command(message: Message, state: FSMContext):
    if str(message.from_user.id) in ADMIN_ID:
        await message.answer(text='Введите нужные даты в формате "05.09, 06.09"')
        # Устанавливаем состояние ожидания ввода дат
        await state.set_state(FSMFillForm.fill_dates)


# Этот хэндлер будет срабатывать на ввод дат
@router.message(StateFilter(FSMFillForm.fill_dates))
async def process_name_sent(message: Message, state: FSMContext, bot=None):
    # сохраняем введенные даты в переменную dates
    dates = message.text
    # отправляем на канал фото + текст в одном сообщении
    await bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=FSInputFile(photo_nails[randint(1, 24)]),
        caption=f'Добрый день! Я, <b>Ирина</b> начинающий мастер по маникюру, ищу моделей для отработки техники и '
                f'скорости по покрытию гель лаком ногтей на: {dates} - начало 10.30 - 12.00, '
                f'длительность процедуры 3,5 - 4 часа.\n<b><u>ОПЛАТА ТОЛЬКО ЗА МАТЕРИАЛЫ - 20зл.</u></b>\n'
                f'Варшава, район Stary Mokotow, метро Racławicka.\n'
                f'Вся информация обо мне, фотографии моих работ, мои контактные данные и другую информацию, '
                f'можно посмотреть у моего бота:\n'
                f'https://t.me/Manicure_Iryna_BOT'
                        )

    # Завершаем машину состояний
    await state.clear()


#  Попытка объединить несколько фото и текст
#  Этот хэндлер будет срабатывать на ввод дат
# @router.message(StateFilter(FSMFillForm.fill_dates))
# async def process_name_sent(message: Message, state: FSMContext, bot=None):
#     # сохраняем введенные даты в переменную dates
#     dates = message.text
#
#     media = types.MediaGroup()
#     media.attach_photo(types.InputFile(photo_nails[randint(1, 24)]))
#     media.attach_photo(types.InputFile(photo_nails[randint(1, 24)]))
#
#     await bot.send_media_group(
#         chat_id=CHANNEL_ID,
#         media=media,
#         caption=f'Добрый день! Я, <b>Ирина</b> начинающий мастер по маникюру, ищу моделей для отработки техники и '
#                 f'скорости по покрытию гель лаком ногтей на: {dates} - начало 10.30 - 12.00, '
#                 f'длительность процедуры 3,5 - 4 часа.\n<b><u>ОПЛАТА ТОЛЬКО ЗА МАТЕРИАЛЫ - 20зл.</u></b>\n'
#                 f'Варшава, район Stary Mokotow, метро Racławicka.\n'
#                 f'Вся информация обо мне, фотографии моих работ, мои контактные данные и другую информацию, '
#                 f'можно посмотреть у моего бота:\n'
#                 f'https://t.me/Manicure_Iryna_BOT'
#                         )
#
#     # Завершаем машину состояний
#     await state.clear()
