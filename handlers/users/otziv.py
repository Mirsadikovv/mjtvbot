from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.otzivKeyboard import otziv
from keyboards.default.menuKeyboard import menu
import logging
# from keyboards.default.pythonKeyboard import menuPython

from loader import dp


@dp.message_handler(text='VIP')
async def send_link(message: Message):
    photo = "https://avatars.mds.yandex.net/i?id=a3b051f13463ab17c8d29bf72f677130-5699340-images-thumbs&n=13"
    await message.answer_photo(photo,caption = "В тариф VIP входит")

@dp.message_handler(text='VIP plus')
async def send_link(message: Message):
    photo = "https://yeasu.ru/wp-content/uploads/6/9/a/69a4fee10d636305dc021a1de8d8304a.png"
    await message.answer_photo(photo,caption = "В тариф VIP plus входит")


@dp.message_handler(text='Назад')
async def send_link(message: Message):
    logging.info(message)
    await message.answer("Выберите одно из следующих:",reply_markup = menu)