from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Мои адреса")],
       
        [KeyboardButton(text = "Отправить геолокацию", request_location = True),  KeyboardButton(text = "Назад")],
    ],
resize_keyboard = True)