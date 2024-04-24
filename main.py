import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

import src.handlers.deciphering as deciphering_module
import src.handlers.fill as fill_module
import src.handlers.help as help_module
import src.handlers.quote as quote_module
import src.handlers.translation as translation_module
import src.handlers.words as words_module
from src.auth_data import token
from src.database import create_db

logging.basicConfig(level=logging.INFO)
create_db()
bot = Bot(token)
dp = Dispatcher()

dp.include_routers(
    help_module.router,
    words_module.router,
    fill_module.router,
    translation_module.router,
    deciphering_module.router,
    quote_module.router,
)
logging.basicConfig(level=logging.INFO)


async def setup_bot_commands():
    await bot.set_my_commands(
        [
            BotCommand(command="/help", description="Get info about me"),
            BotCommand(command="/words", description='Start "Word game"'),
            BotCommand(command="/fill", description='Start "Fill in the blank" game'),
            BotCommand(
                command="/translation", description='Start "Word translation" game'
            ),
            BotCommand(
                command="/deciphering",
                description='Start "Deciphering voice messages" game',
            ),
            BotCommand(
                command="/quote",
                description='Start "Identify the author by a famous quote" game',
            ),
        ]
    )


async def main():
    await setup_bot_commands()
    logging.info("Starting bot")
    await dp.start_polling(bot)
    logging.info("Bot stopped")


if __name__ == "__main__":
    asyncio.run(main())
