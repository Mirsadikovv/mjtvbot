# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
 

# otziv = ReplyKeyboardMarkup(
#     keyboard = [
#         [
#             KeyboardButton(text='Отправить контакт', request_contact=True),
#             KeyboardButton(text='Назад'),
#         ],
#     ],
#     resize_keyboard=True
# )
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
 

otziv = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='VIP'),
            KeyboardButton(text='VIP plus'),
        ],
        [KeyboardButton(text='Назад')]
    ],
    resize_keyboard=True
)