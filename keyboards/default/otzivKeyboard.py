from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
 

otziv = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Отправить контакт', request_contact=True),
            KeyboardButton(text='Назад'),
        ],
    ],
    resize_keyboard=True
)