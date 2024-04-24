from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Hi! I am a bot. Write /help for the command list.")
