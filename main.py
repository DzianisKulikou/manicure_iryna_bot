from environs import Env                             # Позволяет сохранять переменные в окружение
from aiogram import Bot, Dispatcher
from config_data.config import load_config
from handlers import other_handlers, user_handlers   # Импортируем роутеры из хэндлеров


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

# Запрос к серверу на получение абдейтов для бота
if __name__ == '__main__':
    dp.run_polling(bot)
