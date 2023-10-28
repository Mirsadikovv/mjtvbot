from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo


tarif = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='VIP'),
            KeyboardButton(text='Sport'),
        ],
        [KeyboardButton(text='Назад')]
    ],
    resize_keyboard=True
)

tarif_sport = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='VIP'),
            KeyboardButton(text='Sport'),
        ],
        [KeyboardButton(text='Назад')]
    ],
    resize_keyboard=True
)

tarif_VIP = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='VIP', web_app=WebAppInfo(url = "https://i3cpu.github.io/index.html")),
            KeyboardButton(text='Sport'),
        ],
        [KeyboardButton(text='Назад🔙')]
    ],
    resize_keyboard=True
)

tarif_VIPandsport = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='VIP', web_app=WebAppInfo(url = "https://i3cpu.github.io/index.html")),
            KeyboardButton(text='Sport'),
        ],
        [KeyboardButton(text='Назад🔙')]
    ],
    resize_keyboard=True
)











nomer = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Отправить мой номер',request_contact=True),
            
        ],
        
    ],
    resize_keyboard=True
)
