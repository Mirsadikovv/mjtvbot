from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
menu = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Бесплатные каналы🆓", web_app=WebAppInfo(url = "https://i3cpu.github.io/index.html"))],
        [KeyboardButton(text = "Тарифы")],
        [KeyboardButton(text = "Мои подписки✅"),  KeyboardButton(text = "⚙️ Настройки")],
    ],
resize_keyboard = True)

televizor = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text = "Давайте приступим🚀")],
    ],
resize_keyboard = True)