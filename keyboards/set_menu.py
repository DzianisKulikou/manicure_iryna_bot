from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon_ru import lexicon_menu_ru


# Создаем асинхронную функцию для кнопки menu
async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [
        BotCommand(command='/start',
                   description=lexicon_menu_ru['/st']),
        BotCommand(command='/help',
                   description=lexicon_menu_ru['/he'])]

    await bot.set_my_commands(main_menu_commands)
