from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
back_btn=KeyboardButton(text="Назад")

main_kb=ReplyKeyboardMarkup    (
    keyboard=[
      [KeyboardButton(text="Персонаж"),KeyboardButton(text="Рюкзак")],
       [KeyboardButton(text="Навыки"), KeyboardButton(text="Снаряжение")],

    ],
    resize_keyboard=True,
    input_field_placeholder="pupupu"






)
backpack_kb=ReplyKeyboardMarkup    (
    keyboard=[
      [KeyboardButton(text="Оружие"),KeyboardButton(text="Одежда")],
       [KeyboardButton(text="Расходники")],
[back_btn]
    ],
    resize_keyboard=True,
    input_field_placeholder="pupupu"

)

