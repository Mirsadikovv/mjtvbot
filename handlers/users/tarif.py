from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline.product_keys import build_keyboard
from keyboards.default.menuKeyboard import menu
import logging
from loader import dp


@dp.message_handler(text='VIP')
async def send_link(message: Message):
    photo = "https://avatars.mds.yandex.net/i?id=a3b051f13463ab17c8d29bf72f677130-5699340-images-thumbs&n=13"
    await message.answer_photo(photo,caption = "В тариф VIP входит",reply_markup=build_keyboard("VIP"))

@dp.message_handler(text='Sport')
async def send_link(message: Message):
    photo = "https://yeasu.ru/wp-content/uploads/6/9/a/69a4fee10d636305dc021a1de8d8304a.png"
    await message.answer_photo(photo,caption = "В тариф Sport входит",reply_markup=build_keyboard("sport"))


@dp.message_handler(text='Назад')
async def send_link(message: Message):
    logging.info(message)
    await message.answer("Выберите одно из следующих:",reply_markup = menu)