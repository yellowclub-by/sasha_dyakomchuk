from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
def backpuck_kb():
    builder=InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="armor",callback_data="b_1"),
        InlineKeyboardButton(text="sword", callback_data="b_2"),
        InlineKeyboardButton(text="poison", callback_data="b_3"),
        width=1
    )
    return builder.as_markup()

links_kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="саит", url="https://www.dndbeyond.com/?srsltid=AfmBOoo4FaLbRwX38Y16PpJ66gX8bT-3CXSbpSE3Bwc-BKbi6CeBz6__")]
    ]
)
links_kb_v2=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="саит", url="tg://resolve?domain=xvostati1")]
    ]
)