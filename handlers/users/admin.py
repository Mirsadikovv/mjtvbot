import asyncio

from aiogram import types
from aiogram.types import InputFile
from data.config import ADMINS
from loader import dp, db, bot

# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def get_file_id_p(message: types.Message):
#     await message.reply(message.photo[-1].file_id)

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


@dp.message_handler(text="/statistika", user_id=ADMINS)
async def send_statistic_to_admins(message: types.Message):
    pass