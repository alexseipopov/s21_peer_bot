from aiogram import Bot, types, Dispatcher

from config import TOKEN
from crud import *

bot = Bot(TOKEN)
dp = Dispatcher()

button_setup = types.KeyboardButton(text="Управление личными данными")
button_set_birthday = types.KeyboardButton(text="Установить введеную дату как ДР")
mkup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[[button_set_birthday], [button_setup]])

@dp.message(commands=["test1"])
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")
    
@dp.message(command="start")
async def start(mess: types.Message):
    check = select("user", where={"tg_id": mess.from_user.id})
    print(check)
    if not check:
        insert("user", {"tg_id": mess.from_user.id})
        await bot.send_message(mess.from_user.id, "Спасибо за регистрацию. Пожалуйста, заполни данные о себе с помощю команд бота")
    else:
        await bot.send_message(mess.from_user.id, "Спасибо что снова с нами!")


@dp.message(commands="setup")
async def setup(mess: types.Message):
    await mess.reply("??", reply_markup=mkup)

@dp.message(lambda mess: mess.text == "Установить введеную дату как ДР")
async def set_birthday(mess: types.Message):
    print(mess)


if __name__ == "__main__":
    dp.start_polling(bot)