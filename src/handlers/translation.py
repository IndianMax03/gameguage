from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("translation"))
async def translataionHandler(message: Message):
    await message.answer("This is game 3")
