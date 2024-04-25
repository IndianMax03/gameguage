from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Hi! My name is Gameguage. Write /help for the command list.")
