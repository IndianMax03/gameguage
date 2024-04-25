from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from src.database import get_random_speech

router = Router()


class DecipheringVoice(StatesGroup):
    answering = State()


@router.message(Command("deciphering"))
async def deciphering_handler(message: Message, state: FSMContext):

    row_id, text = get_random_speech()
    await message.answer_audio(
        FSInputFile("./volume/speeches/" + str(row_id)), caption="Write this speech"
    )

    await state.set_state(DecipheringVoice.answering)
    await state.update_data(correct_answer=text)


@router.message(DecipheringVoice.answering, F.text)
async def deciphering_answer(message: Message, state: FSMContext):
    if message.text[0] == "/":
        await message.answer("You quit the 'Deciphering' game. 👋 \nType new command again please!")
        await state.clear()
        return

    data = await state.get_data()
    correct_answer = data["correct_answer"]
    if correct_answer == message.text:
        await message.answer("Correct ✅")
        row_id, text = get_random_speech()
        await message.answer_audio(
            FSInputFile("./volume/speeches/" + str(row_id)), caption="Let's continue! 😇\nWhat about this one?"
        )
        await state.set_state(DecipheringVoice.answering)
        await state.update_data(correct_answer=text)
    else:
        await message.answer("Incorrect ❌")
