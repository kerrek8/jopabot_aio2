from keyboards.reply_keyboards.zodiak_kb import zodiak_kb
from keyboards.reply_keyboards.days_kb import days_kb
from aiogram.types import ReplyKeyboardRemove
from loader import dp, bot
from aiogram import types
import untangle
from aiogram.dispatcher.filters import Text
from states.states import horo_states
from config import transcript_dict


@dp.message_handler(commands=['horo'])
async def zodiak(msg: types.Message):
    horo_states.message_to_del = []
    message_to_del = await bot.send_message(msg.chat.id, 'Выберите знак зодиака', reply_markup=zodiak_kb)
    horo_states.message_to_del.append(message_to_del)


@dp.message_handler(Text(equals=['\U00002649', '\U00002648', '\U0000264E', '\U00002651']))
async def hoho(msg: types.Message):
    await horo_states.message_to_del[0].delete()
    horo_states.zod.append(msg.text)
    m = await bot.send_message(msg.chat.id, 'Выберите на какой день вы хотите гороскоп', reply_markup=days_kb)
    horo_states.message_to_del.append(m)
    await bot.delete_message(msg.chat.id, msg.message_id)


@dp.message_handler(
    Text(equals=['\U00002064Сегодня\U00002064', '\U00002064Завтра\U00002064', '\U00002064Послезавтра\U00002064']))
async def send_horo(msg: types.Message):
    await horo_states.message_to_del[1].delete()
    del horo_states.message_to_del[0]
    del horo_states.message_to_del[0]
    await bot.delete_message(msg.chat.id, msg.message_id)
    day = msg.text.replace('\U00002064', '')
    horoscope = untangle.parse('https://ignio.com/r/export/utf/xml/daily/com.xml')
    zod = transcript_dict[horo_states.zod[0]]
    del horo_states.zod[0]
    response = f'horoscope.horo.{zod}.{transcript_dict[day]}.cdata'
    str_response = eval(response)
    await bot.send_message(msg.chat.id, f'<b>Гороскоп для {transcript_dict[zod]} на {day}:</b>\n' + str_response,
                           reply_markup=ReplyKeyboardRemove(), parse_mode='html')
