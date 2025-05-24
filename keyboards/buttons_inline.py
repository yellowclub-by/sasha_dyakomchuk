from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton
def backpuck_kb():
    builder=InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="armor",callback_data="b_1"),
        InlineKeyboardButton(text="sword", callback_data="b_2"),
        InlineKeyboardButton(text="poison", callback_data="b_3"),
        width=1
    )
    return builder.as_markup()