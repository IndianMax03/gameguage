from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from database import get_random_word
from database import check_word

router = Router()


class Words(StatesGroup):
    answering = State()


@router.message(Command("words"))
async def words_handler(message: Message, state: FSMContext):
    word = get_random_word(None, None)
    await message.answer(word)
    await state.clear()
    await state.update_data(last_word=word, excluded_words=set([word]))
    await state.set_state(Words.answering)


@router.message(Words.answering, F.text)
async def words_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    last_word = data["last_word"]
    excluded_words = data["excluded_words"]

    if message.text[0] != last_word[-1]:
        await message.answer("Incorrect first letter :-(")
        return

    if message.text in excluded_words:
        await message.answer("You already said this word")
        return

    if not check_word(message.text):
        await message.answer("This word does not exist")
        return

    excluded_words.add(message.text)
    print(message.text)
    print(message.text[-1])
    word = get_random_word(message.text[-1], excluded_words)

    if word is None:
        await message.answer("I don't know more words. You win!")
        await state.clear()
        return

    await message.answer(word)
    await state.update_data(last_word=word, excluded_words=excluded_words)
