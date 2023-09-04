from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.otzivKeyboard import otziv
from keyboards.default.menuKeyboard import menu
import logging
# from keyboards.default.pythonKeyboard import menuPython

from loader import dp




@dp.message_handler(text='Назад')
async def send_link(message: Message):
    logging.info(message)
    await message.answer("Выберите одно из следующих:",reply_markup = menu)