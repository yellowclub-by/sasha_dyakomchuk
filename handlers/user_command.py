from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command

user_routor=Router()

@user_routor.message(CommandStart())
async def start_cmd(message:types.Message):
    await message.answer("Это бот для РПГ Персонажей. Введите ваше имя?")
    user_text=message.text
@user_routor.message(Command('charecter'), F.text.contains("Персонаж"))
async def Charecter(message:types.Message):
    await message.answer('Ваш персонаж')
@user_routor.message(Command('backpack'), F.text.contains("Рюкзак"))
async def backpack(message:types.Message):
    await message.answer('У вас в рюкзаке')
@user_routor.message(Command('abilite'), F.text.contains("Навыки"))
async def abilite(message:types.Message):
    await message.answer('Вы можете делать')
@user_routor.message(Command('equipment'), F.text.contains("Снаряжение"))
async def equipment(message:types.Message):
    await message.answer('На вас надето')
@user_routor.message(F.text.lower().contains("имя"))
async def echo(message: types.Message):
    user_text = message.text
    name = user_text
    await message.answer(f'Ваше имя {name}')
@user_routor.message(Command('name'), F.text.contains("Имя"))
async def your_name(message:types.Message):
    await message.answer('Введите имя')
# def name1(message:types.Message):
#     name=message.text
#     return name
@user_routor.message(Command('age'), F.text.contains("Возрост"))
async def age(message:types.Message):
    pass
# @user_routor.message(F.text)
# async def echo(message:types.Message):
#     user_text=message.text
#     name=user_text
# #     return name
#     await message.answer(f"Это ваше имя {name}")
# @user_routor.message(F.text=="почему")
# @user_routor.message(F.photo)
# @user_routor.message(F.text.lower()=="почему")
# @user_routor.message(F.text.lower().contains("почему"))
# @user_routor.message(F.text.lower().startswith("почему"))

