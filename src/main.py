import logging
from aiogram import Bot, Dispatcher, executor, types
from auth_data import token

bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hi! I am a bot. Write /help for the command list.")

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply("List of available commands:\n"
                        "/help - show command list\n"
                        "/game1 - start game 1\n"
                        "/game2 - start game 2\n"
                        "/game3 - start game 3\n"
                        "/game4 - start game 4\n"
                        "/game5 - start game 5")


@dp.message_handler(commands=['game1'])
async def game1(message: types.Message):
    await message.reply("This is game 1")

@dp.message_handler(commands=['game2'])
async def game2(message: types.Message):
    await message.reply("This is game 2")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
