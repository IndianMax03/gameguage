from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from src.database import get_random_words_by_locale

router = Router()


class Translation(StatesGroup):
    answer = State()


@router.message(Command("translation"))
async def translataion_handler(message: Message, state: FSMContext):
    en_word, words = get_random_words_by_locale("ru")

    await message.answer("Translate this word\n\n" + en_word)
    await state.update_data(correct_answer=words)
    await state.set_state(Translation.answer)


@router.message(Translation.answer, F.text)
async def translation_answer(message: Message, state: FSMContext):
    if not message.text[0] == "/":
        await message.answer("You quit the game.")
        await state.clear()
        return
    data = await state.get_data()
    correct_answer = data["correct_answer"]
    if message.text in correct_answer:
        await message.answer("Correct ;-)")
        await state.clear()
    else:
        await message.answer("Incorrect :-(")
