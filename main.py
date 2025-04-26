from aiogram import Bot, Dispatcher
import asyncio

token="7802010399:AAGDyS3d1zRw6oMJJSjg6ENDLBRXuIr-R14"
bot=Bot(token=token)
dp=Dispatcher()

from handlers.user_command import user_routor
dp.include_router(user_routor)

async def main():
    print(f"Здравствуй ")
    await dp.start_polling(bot)

asyncio.run(main())

