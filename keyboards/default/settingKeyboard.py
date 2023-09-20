from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

setting = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Профиль'),
            KeyboardButton(text='Язык'),
        ],
        [KeyboardButton(text='Назад')]
    ],
    resize_keyboard=True
)