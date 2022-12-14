from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from crud import *

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(mess: types.Message):
    check = select("user", where={"tg_id": mess.from_user.id})
    print(check)
    if not check:
        insert("user", {"tg_id": mess.from_user.id})
        await mess.reply("Спасибо за регистрацию. Пожалуйста, заполни данные о себе с помощю команд бота")
    else:
        await mess.reply("Спасибо что снова с нами!")

@dp.message_handler(commands="set_birthday")
async def set_birthday(mess: types.Message):
    pass


if __name__ == "__main__":
    executor.start_polling(dp)