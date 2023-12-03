from loader import dp, bot
from aiogram import types
from config import cats
import random


@dp.message_handler(commands=['cat'])
async def cat(messenge: types.Message):
    await bot.send_animation(messenge.chat.id, random.choice(cats))
