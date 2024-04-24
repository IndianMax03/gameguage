from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database import get_random_text_with_gap

router = Router()


class FillingGaps(StatesGroup):
    answering = State()


@router.message(Command("fill"))
async def fill_handler(message: Message, state: FSMContext):
    main_text, missed_text = get_random_text_with_gap()
    await message.answer("Fill the gaps\n\n" + main_text)

    await state.update_data(missed_text=missed_text)
    await state.set_state(FillingGaps.answering)


@router.message(FillingGaps.answering, F.text)
async def fill_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    correct_answer = data["missed_text"]
    if correct_answer == message.text:
        await message.answer("Correct ;-)")
        await state.clear()
    else:
        await message.answer("Incorrect :-(")
