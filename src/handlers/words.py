from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("words"))
async def wordsHandler(message: Message):
    await message.answer("This is game 1")
