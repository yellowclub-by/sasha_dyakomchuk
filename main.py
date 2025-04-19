from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
import asyncio
token="7802010399:AAGDyS3d1zRw6oMJJSjg6ENDLBRXuIr-R14"
bot=Bot(token=token)
dp=Dispatcher()
@dp.message(CommandStart())
async def start_cmd(message:types.Message):
    await message.answer("Это бот для РПГ Персонажей. Введите ваше имя?")
    user_text=message.text
@dp.message()
async def echo(message:types.Message):
    user_text=message.text
    name=user_text
    await message.answer(f"Это ваше имя {name}")
async def main():
    print(f"Здравствуй ")
    await dp.start_polling(bot)
asyncio.run(main())

