from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "🍴 Меню")],
        [KeyboardButton(text = "🛒 Корзина")],
        [KeyboardButton(text = "✍️ Оставить отзыв"),  KeyboardButton(text = "⚙️ Настройки")],
    ],
resize_keyboard = True)