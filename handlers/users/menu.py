from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.otzivKeyboard import otziv
from keyboards.default.settingKeyboard import setting
from keyboards.default.mainKeyboard import main
from keyboards.inline.productsKeyboard import categoryMenu, coursesMenu, booksMenu, telegram_keyboard, algoritm_keyboard
from keyboards.inline.callback_data import course_callback, book_callback

from aiogram.types import Message, CallbackQuery

import logging


from loader import dp


@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    logging.info(message)
    await message.answer("Выберите одно из следующих:", reply_markup=menu)


@dp.message_handler(text='🍴 Меню')
async def send_link(message: Message):
    logging.info(message)
    await message.answer("<b>Вот наше меню!</b>",reply_markup = categoryMenu)


@dp.message_handler(text='✍️ Оставить отзыв')
async def send_link(message: Message):
    await message.answer("Сначала отправьте номер телефона чтобы мы смогли связаться с вами!",reply_markup = otziv)


@dp.message_handler(text='⚙️ Настройки')
async def send_link(message: Message):
    await message.answer("Выберите язык:",reply_markup = setting)


@dp.message_handler(text='🛒 Корзина')
async def send_link(message: Message):
    await message.answer("Вы совсем ничего не заказали.",reply_markup = menu)







@dp.callback_query_handler(text="courses")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Kurs tanlang", reply_markup=coursesMenu)
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="books")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Kurs tanlang", reply_markup=booksMenu)
    await call.answer(cache_time=60)




@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz

    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer()




@dp.callback_query_handler(course_callback.filter(item_name="telegram"))
async def buying_course(call: CallbackQuery, callback_data: dict):

    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")

    await call.message.answer(f"Siz Mukammal Telegram Bot Kursini tanladingiz.",
                              reply_markup=telegram_keyboard)

    await call.answer(cache_time=60)

@dp.callback_query_handler(book_callback.filter(item_name="python_book"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=20, show_alert=True)