from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards.reply_keyboards.games_kb import games_kb



@dp.message_handler(commands=['game'])
async def games(msg: types.Message):
    await bot.send_message(msg.chat.id, 'Выберите игру', reply_markup=games_kb)


@dp.message_handler(Text(equals='\U00002064Кости\U00002064'))
async def dice_game(msg: types.Message):
    await bot.send_dice(msg.chat.id)


@dp.message_handler(Text(equals='\U00002064Автомат\U00002064'))
async def avto_game(msg: types.Message):
    await bot.send_dice(msg.chat.id, emoji='🎰')


@dp.message_handler(Text(equals='\U00002064Дартс\U00002064'))
async def dart_game(msg: types.Message):
    await bot.send_dice(msg.chat.id, emoji='🎯')


@dp.message_handler(Text(equals='\U00002064Баскетбол\U00002064'))
async def basket_game(msg: types.Message):
    await bot.send_dice(msg.chat.id, emoji='🏀')


@dp.message_handler(Text(equals='\U00002064Футбол\U00002064'))
async def football_game(msg: types.Message):
    await bot.send_dice(msg.chat.id, emoji='⚽')
