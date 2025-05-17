from aiogram import types, Router, F
group_routor=Router()

ban_words=["Негр","Гей","Я","1488","11.09","Гитлер","НЕХОРОШИЙ","Привет!"]

@group_routor.message()
async def cleaner(message: types.Message):
    word_list=message.text.split(" ")
    for word in word_list:
        if word in ban_words:
            await message.delete()
            await message.answer(f"{message.from_user.first_name} п0шел вон!")
            break