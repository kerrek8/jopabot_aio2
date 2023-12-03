from aiogram import types
from config import ap
import random
from loader import dp, bot


@dp.message_handler(commands=['ap'])
async def arturito(msg: types.Message):
    await bot.send_video(msg.chat.id, random.choice(ap))
