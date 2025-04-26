from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_routor=Router()

@user_routor.message(CommandStart())
async def start_cmd(message:types.Message):
    await message.answer("Это бот для РПГ Персонажей. Введите ваше имя?")
    user_text=message.text
@user_routor.message(Command('charecter'))
async def Charecter(message:types.Message):
    await message.answer('Ваш персонаж')
@user_routor.message(Command('backpack'))
async def backpack(message:types.Message):
    await message.answer('У вас в рюкзаке')
@user_routor.message(Command('abilite'))
async def abilite(message:types.Message):
    await message.answer('Вы можете делать')
@user_routor.message(Command('equipment'))
async def equipment(message:types.Message):
    await message.answer('На вас надето')
@user_routor.message(Command('name'))
async def your_name(message:types.Message):
    await message.answer('Введите имя')
    # name = name1()
    # await message.answer(f'Ваше имя {name}')
# def name1(message:types.Message):
#     name=message.text
#     return name
@user_routor.message(Command('age'))
async def age(message:types.Message):
    pass
# @user_routor.message()
# async def echo(message:types.Message):
#     user_text=message.text
#     name=user_text
#     return name
#     await message.answer(f"Это ваше имя {name}")