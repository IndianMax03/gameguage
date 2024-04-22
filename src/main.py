import logging
from auth_data import token
from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_polling

bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я бот. Напиши /help для списка команд.")

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply("Список доступных команд:\n"
                        "/help - показать список команд\n"
                        "/game1 - запустить игру 1\n"
                        "/game2 - запустить игру 2\n"
                        "/game3 - запустить игру 3\n"
                        "/game4 - запустить игру 4\n"
                        "/game5 - запустить игру 5")


@dp.message_handler(commands=['game1'])
async def game1(message: types.Message):
    await message.reply("Это игра 1")

@dp.message_handler(commands=['game2'])
async def game2(message: types.Message):
    await message.reply("Это игра 2")


if __name__ == '__main__':
    start_polling(dp, skip_updates=True)
