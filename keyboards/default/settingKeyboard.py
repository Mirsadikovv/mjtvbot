from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

setting = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Узбекский'),
            KeyboardButton(text='Русский'),
        ],
        [KeyboardButton(text='Назад')]
    ],
    resize_keyboard=True
)