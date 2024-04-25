from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from src.database import get_random_word
from translatepy.translators.google import GoogleTranslate

router = Router()


class Translation(StatesGroup):
    answer = State()
    translator = GoogleTranslate()


@router.message(Command("translation"))
async def translataion_handler(message: Message, state: FSMContext):
    en_word = get_random_word(None, None)
    await message.answer("Translate this word\n\n" + en_word)
    await state.update_data(correct_answer=Translation.translator.translate(en_word, destination_language='Russia').result)
    await state.set_state(Translation.answer)


@router.message(Translation.answer, F.text)
async def translation_answer(message: Message, state: FSMContext):
    if message.text[0] == "/":
        await message.answer("You quit the 'Translation' game. 👋 \nType new command again please!")
        await state.clear()
        return
    data = await state.get_data()
    correct_answer = data["correct_answer"]
    if message.text.lower() == correct_answer.lower():
        await message.answer("Correct ✅")
        en_word = get_random_word(None, None)
        await message.answer("Excellent! What about this?\n\n" + en_word)
        await state.update_data(correct_answer=Translation.translator.translate(en_word, destination_language='Russia').result)
        await state.set_state(Translation.answer)
    else:
        await message.answer("Incorrect ❌")
