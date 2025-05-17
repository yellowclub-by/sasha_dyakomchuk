from keyboards import buttons_reply
from aiogram import types, Router, F
from aiogram.types import FSInputFile

things_routor=Router()

@things_routor.message(F.text.lower()=="оружие")
async def weapon(message: types.Message):
    photo=FSInputFile(r'Images\Eqeupment\sword.jpeg')
    await message.answer_photo(photo, caption="Меч")
    await message.answer("Здесь ваше оружее", reply_markup=buttons_reply.main_kb,)
@things_routor.message(F.text.lower()=="одежда")
async def weapon(message: types.Message):
    photo = FSInputFile(r'Images\Eqeupment\armor.jpeg')
    await message.answer_photo(photo, caption="Броня")
    await message.answer("Вы одеты в ", reply_markup=buttons_reply.main_kb)
@things_routor.message(F.text.lower()=="расходники")
async def weapon(message: types.Message):
    photo = FSInputFile(r'Images\Eqeupment\poison.jpeg')
    await message.answer_photo(photo, caption="Зелье")
    await message.answer("Вы можете использовать ", reply_markup=buttons_reply.main_kb)