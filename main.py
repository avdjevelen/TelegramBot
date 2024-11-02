import asyncio
import logging

from aiogram import Bot, Dispatcher, types
import config
from routers import router as main_router

# Initialize dispatcher
dp = Dispatcher()


async def main():
    dp = Dispatcher()
    dp.include_router(main_router)

    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
