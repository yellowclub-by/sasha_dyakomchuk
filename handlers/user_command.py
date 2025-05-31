from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from keyboards import buttons_reply, buttons_inline
from aiogram.types import FSInputFile
user_routor=Router()

@user_routor.message(CommandStart())
async def start_cmd(message:types.Message):
    await message.answer("Это бот для РПГ Персонажей",reply_markup=buttons_reply.main_kb)
    user_text=message.text
@user_routor.message(Command('charecter'))
@user_routor.message(F.text.lower()=="персонаж")
async def Charecter(message:types.Message):
    await message.answer('Ваш персонаж', reply_markup=buttons_inline.links_kb_v2)
@user_routor.message(Command('backpack'))
@user_routor.message(F.text.lower()=="рюкзак")
async def backpack(message:types.Message):
    await message.answer('У вас в рюкзаке', reply_markup=buttons_inline.backpuck_kb())

@user_routor.callback_query(F.data.startswith("b"))
async def back_puck(callback:types.CallbackQuery):
    dfgh=callback.data.split("_")[1]
    if dfgh=="2":
        await callback.message.answer("Меч \n Урон:2")
        photo = FSInputFile(r'Images\Eqeupment\sword.jpeg')
        await callback.message.answer_photo(photo, caption="Меч")
    elif dfgh=="1":
        await callback.message.answer("Броня \n Защита:2")
        photo = FSInputFile(r'Images\Eqeupment\armor.jpeg')
        await callback.message.answer_photo(photo, caption="Броня")
    elif dfgh=="3":
        await callback.message.answer("Зелье \n +2 Хп")
        photo = FSInputFile(r'Images\Eqeupment\poison.jpeg')
        await callback.message.answer_photo(photo, caption="Зелье")

    await callback.answer("")

@user_routor.message(Command('abilite'))
@user_routor.message(F.text.lower()=="навыки")
async def abilite(message:types.Message):
    await message.answer('Вы можете делать', reply_markup=buttons_inline.links_kb)

    await message.answer("""
    <b> Жирный </b>
    <u> Жирный </u>
    <i> Жирный </i>
    <tg-spoiler> Жирный </tg-spoiler>
    <code> Жирный </code>
    """)
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
@user_routor.message(F.text.lower()=="назад")
async def back(message: types.Message):
    await message.answer("Окей, так уж и быть", reply_markup=buttons_reply.main_kb)
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

