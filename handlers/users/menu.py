from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.tarifKeyboard import tarif
from keyboards.default.settingKeyboard import setting

import logging
from loader import dp,db,bot


# @dp.message_handler(text = "Давайте приступим🚀")
# async def show_menu(message: Message):
#     logging.info(message)
#     await message.delete()
#     await message.answer("Выберите одно из следующих:", reply_markup=menu)



@dp.message_handler(text='Тарифы')
async def send_link(message: Message):
    await message.answer("Вот наши платные тарифы",reply_markup = tarif)


@dp.message_handler(text='Мои подписки')
async def send_link(message: Message):
    user = await db.select_user_status(telegram_id = message.from_user.id)
    for i in user:
        if i == None:
           await message.answer("В данный момент у вас нет активных подписок",reply_markup = menu)
        elif i == "VIP":
            await message.answer("У вас подписка VIP",reply_markup = menu)
        elif i == "Sport":
            await message.answer("У вас подписка Sport",reply_markup = menu)
        break


@dp.message_handler(text='⚙️ Настройки')
async def send_link(message: Message):
    await message.answer("Выберите что хотите изменить:",reply_markup = setting)

@dp.message_handler(text='Назад')
async def send_link(message: Message):
    await message.answer(text = "Выберите действие:", reply_markup = menu)

