from loader import dp, bot
from aiogram import types
from handlers.users.jokes import get_random_anek
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from keyboards.reply_keyboards.anek_kb import anek_kb
from states.states import anek_state
import random


@dp.message_handler(commands='jokes')
async def jokes(msg: types.Message):
    await bot.send_message(msg.chat.id, 'Выберите интересующею вас опцию', reply_markup=anek_kb)


@dp.message_handler(Text(equals='\U00002064Выход\U00002064'))
async def anek_final(msg: types.Message):
    await bot.send_message(msg.chat.id, 'Хорошего настроения', reply_markup=ReplyKeyboardRemove())
    if anek_state.id_a != 0:
        anek_state.id_a = 0


@dp.message_handler(Text(equals='\U00002064Случайный анекдот\U00002064'))
async def rand_anek(msg: types.Message):
  id_anek = random.randint(1, 1940)
  try:
    anek_state.id_a = id_anek
    await bot.send_message(msg.chat.id, get_random_anek.jokes(anek_state.id_a))
  except Exception as ex:
    print(ex)

@dp.message_handler(Text(equals='\U00002064Предыдущий анекдот\U00002064'))
async def prev_anek(msg: types.Message):
    anek_state.id_a -= 1
    await bot.send_message(msg.chat.id, get_random_anek.jokes(anek_state.id_a))


@dp.message_handler(Text(equals='\U00002064Следующий анекдот\U00002064'))
async def next_anek(msg: types.Message):
    anek_state.id_a += 1
    await bot.send_message(msg.chat.id, get_random_anek.jokes(anek_state.id_a))
