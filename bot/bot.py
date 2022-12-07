import logging
from datetime import datetime, timedelta

import openpyxl
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from db.bot.Users import Users

from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputMediaPhoto
from openpyxl.styles import Font

# import keyboards as kb
# import time_function
# from db import db, break_time, dinner_time, speciality, holiday
# from states import speciality, broadcast, bot, work, finance

# Configure logging
import config



logging.basicConfig(filename='logs.txt', level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

users = Users()


# приветсвиное сообщение
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    # await message.answer("del", reply_markup=types.ReplyKeyboardRemove())
    # answer = message.text
    # print(answer)
    json = message
    text = message.from_user.id
    print(text)
    print(json)
    await message.answer("test bot")
    #
    # # greet_kb.add(webapp_keyboard2)
    # logging.info(f"{message.answer}нажали старт")
    #
    # if db.checkRegistration(message.from_user.id) == 1:
    #     await message.answer("Вы уже зарегистрированны")
    # else:
    #     await message.answer(
    #         'Приветсвую это рабочий бот badm-store\n'
    #         'Бот используется в личных целях компании.Для доступа к функционалу вам необходимо ввести код доступа\n\n'
    #         '<b>Введи код:</b>',
    #         parse_mode='HTML')


@dp.message_handler(commands="users")
async def cmd_start(message: types.Message):
    await message.answer(users.get_all_users())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
