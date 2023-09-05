from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import logging
from loader import dp
from states.personalData import PersonalData
from aiogram.dispatcher import FSMContext



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    await message.answer(f"""Привет, {message.from_user.full_name}!
Добро пожаловать в тв-бот""")
    await message.answer("Введите ваше полное имя:")
    await PersonalData.fullName.set()



@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text
    if len(fullname)<3 or not fullname.isalpha():
        await message.answer("Ваше имя слишком короткое либо не корректное!")
        await PersonalData.fullName.set()
    else:   
        await state.update_data(
            {"name": fullname}
        )

        await message.answer("Введите ваш Email:")

        # await PersonalData.email.set()
        await PersonalData.next()

@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state: FSMContext):
    email = message.text

    await state.update_data(
        {"email": email}
    )

    await message.answer("Введите ваш номер телефона:")
    
    await PersonalData.next()


@dp.message_handler(state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text
    if len(phone)<9 or not phone.isdigit():
        await message.answer("Ваше номер слишком короткий или не корректный!")
        await PersonalData.phoneNum.set()
    else:   
        await state.update_data({"phone": phone})
        # Ma`lumotlarni qayta o'qiymiz
        data = await state.get_data()
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")

        msg = "Ваши данные:\n"
        msg += f"Ismingiz - {name}\n"
        msg += f"Email - {email}\n"
        msg += f"Telefon - {phone}"
        await message.answer(msg)

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