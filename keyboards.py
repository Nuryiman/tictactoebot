from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

fields_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=".", callback_data="field"),
            InlineKeyboardButton(text=".", callback_data="field"),
            InlineKeyboardButton(text=".", callback_data="field"),
        ],
        [
            InlineKeyboardButton(text=".", callback_data="field"),
            InlineKeyboardButton(text=".", callback_data="field"),
            InlineKeyboardButton(text=".", callback_data="field"),
        ],
        [
            InlineKeyboardButton(text=".", callback_data="field"),
            InlineKeyboardButton(text=".", callback_data="field"),
            InlineKeyboardButton(text=".", callback_data="field"),
        ]
    ]
)

request_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Принять вызов", callback_data="vyzov"),
        ],
    ]
)
cancel_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ]
)