from aiogram import Bot, Dispatcher
import asyncio

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

token="7802010399:AAGDyS3d1zRw6oMJJSjg6ENDLBRXuIr-R14"
bot=Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp=Dispatcher()

from handlers.user_command import user_routor
dp.include_router(user_routor)
from handlers.things import things_routor
dp.include_router(things_routor)
from handlers.group_command import group_routor
dp.include_router(group_routor)

async def main():
    print(f"Здравствуй ")
    await dp.start_polling(bot)

asyncio.run(main())

