from loader import dp, bot
from aiogram import types
from config import world_tour
import random


@dp.message_handler(commands=['world_tour'])
async def dubai(messenge: types.Message):
    rand_k = random.choice(list(world_tour))
    await bot.send_photo(messenge.chat.id, world_tour[rand_k], caption=f'Вы попали {rand_k}')
