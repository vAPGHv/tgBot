# -------=imports=-------
from settings import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests as req
from bs4 import BeautifulSoup as BS
import random
from time import sleep
from getimg import getimg

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

t = 3


# -------=start bot=-------
@dp.message_handler(commands=["start"])
async def startMe(message: types.message):
    try:

        imgbut = KeyboardButton("/img your message")
        menu = ReplyKeyboardMarkup(resize_keyboard=True).add(imgbut)

        await bot.send_message(message.chat.id, "Hello! Im moderator ( enter /img cat) )", reply_markup=menu)

    except:
        print("none")
        return "none"


# -------=bot functions=-------
@dp.message_handler()
async def myBot(message: types.Message):
    try:

        lowerm = message.text.lower()

        for i in cens:
            if i in lowerm:
                await message.delete()
                return "no!"

        sleep(t)

        # -------=img bot=-------

        if "/img" in message.text[0:4]:
            reg = message.text.split("/img ", maxsplit=1)[1]  # get the word after the command
            print(reg)
            getimg(reg)

            with open('img.jpg', 'rb') as photo:
                await bot.send_photo(message.chat.id, photo)

    except Exception as ex:
        await bot.send_message(message.chat.id, ex)
        print(ex)
        return ex


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
