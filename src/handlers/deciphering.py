from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("deciphering"))
async def decipheringHandler(message: Message):
    await message.answer("This is game 4")
