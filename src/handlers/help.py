from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "List of available commands:\n"
        "/help - show command list\n"
        "/words - start 'Word game'\n"
        "/fill - start 'Fill in the blank' game\n"
        "/translation - start 'Word translation' game\n"
        "/deciphering - start 'Deciphering voice messages' game\n"
        "/quote - start 'Identify the author by a famous quote' game\n"
    )
