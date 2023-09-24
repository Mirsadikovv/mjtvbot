from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import logging
from loader import dp,db,bot
from states.personalData import PersonalData
from aiogram.dispatcher import FSMContext
import asyncpg 
from data.config import ADMINS
from keyboards.default.otzivKeyboard import nomer


from keyboards.default.menuKeyboard import televizor



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username
                                 )
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)


    logging.info(message)
    await message.answer(f"""Привет, {message.from_user.full_name}!
Добро пожаловать в тв-бот""")
    
    # ADMINGA xabar beramiz
    count = await db.count_users()
    msg = f"{user[1]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)


    await message.answer(text = "Чтобы использовать бота отправьте нам номер телефона)",reply_markup = nomer)
    await PersonalData.phoneNum.set()



# @dp.message_handler(state=PersonalData.fullName)
# async def answer_fullname(message: types.Message, state: FSMContext):
#     fullname = message.text
#     if len(fullname)<3 or not fullname.isalpha():
#         await message.answer("Ваше имя слишком короткое либо не корректное!")
#         await PersonalData.fullName.set()
#     else:   
#         await state.update_data(
#             {"name": fullname}
#         )

#         await message.answer("Введите ваш Email:")

#         # await PersonalData.email.set()
#         await PersonalData.next()

# @dp.message_handler(state=PersonalData.email)
# async def answer_email(message: types.Message, state: FSMContext):
#     email = message.text

#     await state.update_data(
#         {"email": email}
#     )

#     await message.answer("Введите ваш номер телефона:", reply_markup=nomer)
    
#     await PersonalData.next()


@dp.message_handler(content_types=[types.ContentType.CONTACT],state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    # phone = message.text
    contact = message.contact
    phone = contact.phone_number
    print(phone)
    # if len(phone)<9 or not phone.isdigit():
    #     await message.answer("Ваше номер слишком короткий или не корректный!")
    #     await PersonalData.phoneNum.set()
    # else:   
    await state.update_data({"phone": phone})
        # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    # name = data.get("name")
    # email = data.get("email")
    phone = data.get("phone")
    await db.update_user_phone(phone = str(phone), telegram_id=message.from_user.id)
    msg = "Ваши данные:\n"
    msg += f"Ismingiz - {message.from_user.full_name}\n"
    # msg += f"Email - {email}\n"
    msg += f"Telefon - {phone}"
    await message.answer(msg, reply_markup=televizor)

    # State dan chiqaramiz
    # 1-variant

    await state.finish()

# @dp.message_handler(content_types=['photo'])
# async def process_photo(message: types.Message):
#     # Получение файла из сообщения
#     photo = await message.photo[-1].download()
    
#     # Обработка файла
#     # Отправка обработанного фото
#     await message.reply_photo(photo)