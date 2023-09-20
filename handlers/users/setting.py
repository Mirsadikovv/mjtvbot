from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.settingKeyboard import setting
from keyboards.default.menuKeyboard import menu
import logging
from states.personalData import PersonalData
# from keyboards.default.pythonKeyboard import menuPython

from loader import dp


@dp.message_handler(text='Профиль')
async def send_link(message: Message):
    await message.answer(text = "Введите ваше полное имя:")
    await PersonalData.fullName.set()

@dp.message_handler(text='Язык')
async def send_link(message: Message):
    await message.answer(text = "На данный момент наш бот работает только на русском")


@dp.message_handler(text='Назад')
async def send_link(message: Message):
    logging.info(message)
    await message.answer("Выберите одно из следующих:",reply_markup = menu)