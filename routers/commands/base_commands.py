from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown

router = Router(name=__name__)

with open("routers/text.txt", "r", encoding="utf-8") as file:
    text = file.read()


@router.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        text=f"Hello, {markdown.hbold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML,
    )


@router.message(Command("help", prefix="!/"))
async def handle_help(message: types.Message):
    await message.answer(
        text=f"{markdown.hbold(text)}",
        parse_mode=ParseMode.HTML,
    )
