from aiogram import Bot
from aiogram.types import BotCommand


# Создаем асинхронную функцию для кнопки menu
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Запусти меня с начала!'),
        BotCommand(command='/help',
                   description='Справка по работе бота')]

    await bot.set_my_commands(main_menu_commands)