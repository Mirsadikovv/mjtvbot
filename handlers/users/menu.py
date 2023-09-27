from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.otzivKeyboard import otziv
from keyboards.default.settingKeyboard import setting
from keyboards.default.mainKeyboard import main
from keyboards.inline.productsKeyboard import categoryMenu
# from keyboards.inline.callback_data import course_callback, book_callback
# from states.personalData import PersonalData
# from aiogram.types import Message, CallbackQuery
import logging
from loader import dp,db,bot


@dp.message_handler(text = "Televizor")
async def show_menu(message: Message):
    logging.info(message)
    await message.answer("Выберите одно из следующих:", reply_markup=menu)

@dp.message_handler(text='Бесплатные каналы')
async def send_link(message: Message):
    logging.info(message)
    await message.answer("<b>Вот наше меню!</b>",reply_markup = categoryMenu)

@dp.message_handler(text='Тарифы')
async def send_link(message: Message):
    await message.answer("Вот наши платные тарифы",reply_markup = otziv)

@dp.message_handler(text='Мои подписки')
async def send_link(message: Message):
    user = await db.select_user_status(telegram_id = message.from_user.id)
    for i in user:
        if i == None:
           await message.answer("В данный момент у вас нет активных подписок",reply_markup = menu)
        elif i == "VIP":
            await message.answer("У вас подписка VIP",reply_markup = menu)
        elif i == "VIP plus":
            await message.answer("У вас подписка VIP plus",reply_markup = menu)
        break


@dp.message_handler(text='⚙️ Настройки')
async def send_link(message: Message):
    await message.answer("Выберите что хотите изменить:",reply_markup = setting)

@dp.message_handler(text='Назад')
async def send_link(message: Message):
    await message.answer(text = "Выберите действие:", reply_markup = menu)

