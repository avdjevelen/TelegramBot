from aiogram import F, Router, types
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove

import random

router = Router(name=__name__)

# Load phrases into a list


# @router.message()
# async def comment_on_group(message: types.Message):
#     # Check if message is from a group or channel
#     if message.chat.type in ["group", "supergroup", "channel"]:
#         # Select a random phrase
#         response = random.choice(phrases).strip()  # Remove any newline characters
#
#         # Reply to the post
#         await message.reply(response)


# @router.channel_post()
# async def comment_on_post(message: types.Message):
#     # Select a random phrase and strip any newline characters
#     response = random.choice(phrases).strip()
#
#     # Reply to the channel post to simulate a "comment"
#     await message.reply(response)
