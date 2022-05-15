# -------=imports=-------
from settings import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests as req
from bs4 import BeautifulSoup as BS
import random
from time import sleep

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

t = 3


# -------=start bot=-------
@dp.message_handler(commands=["start"])
async def startMe(message: types.message):
    try:

        imgbut = KeyboardButton("/img ваше сообщение")
        menu = ReplyKeyboardMarkup(resize_keyboard=True).add(imgbut)

        await bot.send_message(message.chat.id, "Привет! Я бот модератор! (кстати если ввести /img то получишь изображение на тему того что написал после /img)", reply_markup=menu)

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

        if "/img " in message.text:
            reg = message.text.split("/img ")[1]  # get the word after the command
            url = f"https://www.google.com/search?q={reg}&client=opera&hs=nkI&hl=ru&sxsrf=APq-WBuUWCpyLYYduHWl9vqF9dG_IIvdpg:1649445742756&source=lnms&tbm=isch&sa=X&ved=2ahUKEwizzsqcmIX3AhVM-yoKHcKBCg0Q_AUoAXoECAEQAw&biw=2519&bih=1299&dpr=1"

            r = req.get(url)

            soup = BS(r.content, "html.parser")
            list1 = []

            for i in soup.select("img", class_="Q4LuWd"):
                list1.append(i.get("src"))

            randel = list1[random.randrange(1, len(list1))]
            randel = req.get(randel).content

            with open(f"123.jpg", "wb") as file:
                file.write(randel)

            hoto = open('123.jpg', 'rb')
            await bot.send_photo(message.chat.id, hoto)

    except:
        print("none")
        return "none"


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
