from environs import Env                             # Позволяет сохранять переменные в окружение
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command, BaseFilter

env = Env()              # Создаем экземпляр класса Env
env.read_env()           # Методом read_env() читаем файл .env и загружаем из него переменные в окружение

bot_token = env('bot_token')       # Сохраняем значение переменной окружения в переменную bot_token

# Создаем объекты бота и диспетчера
bot: Bot = Bot(bot_token)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЯ бот Ирины Куликовой\n'
                         'Я могу рассказать вам всю информацию о её деятельности мастером по маникюру')
    print(message.from_user.id)

# Запрос к серверу на получение абдейтов для бота
if __name__ == '__main__':
    dp.run_polling(bot)
