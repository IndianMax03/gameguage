from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from database import get_random_speech

router = Router()


class DecipheringVoice(StatesGroup):
    answering = State()


@router.message(Command("deciphering"))
async def deciphering_handler(message: Message, state: FSMContext):

    rowid, text = get_random_speech()
    await message.answer_audio(FSInputFile("./volume/speeches/" + str(rowid)))

    await state.set_state(DecipheringVoice.answering)
    await state.update_data(correct_answer=text)


@router.message(DecipheringVoice.answering, F.text)
async def deciphering_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    correct_answer = data["correct_answer"]
    if correct_answer == message.text:
        await message.answer("Correct ;-)")
        await state.clear()
    else:
        await message.answer("Incorrect :-(")
