from aiogram import F, Router, types
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

import random

router = Router(name=__name__)

phrases = [
    "Great post!",
    "Interesting!",
    "Thanks for sharing!",
    "Well said!",
    "Totally agree!",
    "Nice one!",
]


@router.message()
async def comment_on_post(message: types.Message):
    # Skip bot messages to avoid self-reply loops
    if message.from_user.is_bot:
        return

    # Select a random phrase
    response = random.choice(phrases)

    # Reply to the post
    await message.answer(response)
