import asyncio

from aiogram import types
from aiogram.types import InputFile
from data.config import ADMINS
from loader import dp, db, bot


@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = await db.select_all_users()
    photo_file = "AgACAgIAAxkBAAIFhmUUR_bj0Ipe4azYDN3-0vWUe25BAALG0jEbRMqgSL_L3iwnfmPEAQADAgADeAADMAQ"
    # print(photo_file)
    
    for user in users:
        # print(user[3])
        user_id = user[3]
        await bot.send_photo(photo=photo_file, chat_id=user_id, caption="<a href = 'https://t.me/hajimeN1'>Подпишись!</a>")
        await asyncio.sleep(0.05)


@dp.message_handler(text="/stat", user_id=ADMINS)
async def send_statistic_to_admins(message: types.Message):
    file1 = open("baza.txt","w")
    users = await db.select_all_users()
    for i in users:
        file1.write(f"{i}\n\n")
    count = await db.count_users()
    with open('baza.txt', 'rb') as file1:
        await bot.send_document(message.from_user.id, file1,caption =f"В данный момент в нашей базе {count} пользователя")
        
   

