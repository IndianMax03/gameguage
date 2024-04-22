import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.router import Router
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram import F

from auth_data import token

logging.basicConfig(level=logging.INFO)
bot = Bot(token)
dp = Dispatcher()
router = Router()
dp.include_routers(router)
logging.basicConfig(level=logging.INFO)

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Hi! I am a bot. Write /help for the command list.')

@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer('List of available commands:\n'
                        '/help - show command list\n'
                        '/game1 - start game 1\n'
                        '/game2 - start game 2\n'
                        '/game3 - start game 3\n'
                        '/game4 - start game 4\n'
                        '/game5 - start game 5')


@dp.message(Command('game1'))
async def game1(message: types.Message):
    await message.answer('This is game 1')

@dp.message(Command('game2'))
async def game2(message: types.Message):
    await message.answer('This is game 2')

@dp.message(Command('game3'))
async def game2(message: types.Message):
    await message.answer('This is game 3')

@dp.message(Command('game4'))
async def game2(message: types.Message):
    await message.answer('This is game 4')

@dp.message(Command('game5'))
async def game2(message: types.Message):
    await message.answer('This is game 5')

@router.message(F.text)
async def any(message: Message):
    await message.reply('Invalid input text')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
