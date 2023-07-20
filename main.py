from environs import Env                             # Позволяет сохранять переменные в окружение
from aiogram import Bot, Dispatcher
from config_data.config import load_config
from handlers import other_handlers, user_handlers   # Импортируем роутеры из хэндлеров
from aiogram.types import BotCommand


env = Env()              # Создаем экземпляр класса Env
env.read_env()           # Методом read_env() читаем файл .env и загружаем из него переменные в окружение

config = load_config('.env>')
bot_token = env('bot_token')       # Сохраняем значение переменной окружения в переменную bot_token

# Создаем объекты бота и диспетчера
bot: Bot = Bot(config.tg_bot.token)
dp: Dispatcher = Dispatcher()

# Регистрируем роутеры в диспетчере
dp.include_router(user_handlers.router)
dp.include_router(other_handlers.router)


# Создаем асинхронную функцию для кнопки menu
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Запусти меня с начала!'),
        BotCommand(command='/help',
                   description='Справка по работе бота')]

    await bot.set_my_commands(main_menu_commands)


# Запрос к серверу на получение абдейтов для бота
if __name__ == '__main__':
    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота,
    dp.startup.register(set_main_menu)
    # Запускаем поллинг
    dp.run_polling(bot)
