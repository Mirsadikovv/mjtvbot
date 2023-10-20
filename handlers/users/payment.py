from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from data.config import ADMINS

from loader import dp, bot
from data.products import ds_vip, ds_sport
from keyboards.inline.product_keys import build_keyboard


@dp.message_handler(Command("VIP"))
async def show_invoices(message: types.Message):
    caption = "<b>Подписка VIP</b> .\n\n"
    caption += "Цена: <b>25 000 сум</b>\n"
    caption += "Скидка от админа: <b>-6 000 сум</b>"
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=e4e2d6728f62814504ae458a29efaafe-4265706-images-thumbs&n=13",
                         caption=caption, reply_markup=build_keyboard("VIP"))

@dp.message_handler(Command("sport"))
async def show_invoices(message: types.Message):
    caption = "<b>Подписка Sport</b> .\n\n"
    caption += "Цена: <b>20 000 сум</b>\n"
    caption += "Скидка от админа: <b>-5 000 сум</b>"
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=aa319fae26d038194a903b6c48b0780d4054b34f-9844228-images-thumbs&n=13",
                         caption=caption, reply_markup=build_keyboard("sport"))



@dp.callback_query_handler(text="product:VIP")
async def VIP_plus_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **ds_vip.generate_invoice(),
                           payload="payload:VIP")
    await call.answer()

@dp.callback_query_handler(text="product:sport")
async def VIP_plus_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **ds_sport.generate_invoice(),
                           payload="payload:sport")
    await call.answer()



@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Спасибо за покупку!")
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Куплено: {pre_checkout_query.invoice_payload}\n"
                                f"ID: {pre_checkout_query.id}\n"
                                f"Пользователь: {pre_checkout_query.from_user.first_name}\n"                                
                                f"Покупатель: {pre_checkout_query.order_info.name}, тел: {pre_checkout_query.order_info.phone_number}\n\n"
                                f"Telegram id: {pre_checkout_query.from_user.id}\n")