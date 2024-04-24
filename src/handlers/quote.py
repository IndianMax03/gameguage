from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database import get_random_book_quotes

router = Router()


class Quote(StatesGroup):
    answering = State()


@router.message(Command("quote"))
async def quote_handler(message: Message, state: FSMContext):
    result_list = get_random_book_quotes(5)
    quote = result_list[0][0]

    builder = InlineKeyboardBuilder()
    for row in result_list:
        builder.add(InlineKeyboardButton(text=row[1], callback_data=row[1]))

    await message.answer(quote, reply_markup=builder.as_markup())
    await state.update_data(correct_answer=result_list[0][1], quote=quote)
    await state.set_state(Quote.answering)


@router.callback_query(Quote.answering)
async def quote_callback(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    correct_answer = data["correct_answer"]
    quote = data["quote"]
    if callback.data == correct_answer:
        await state.clear()
        await callback.answer(text="Correct ;-)")
        await callback.message.edit_text(text=f"{quote} is from {correct_answer}")
    else:
        await callback.answer(text="Incorrect :-(")
