from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
 

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

nomer = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Отправить мой номер',request_contact=True),
            
        ],
        
    ],
    resize_keyboard=True
)
