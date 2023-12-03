from handlers.users.sovmestimost import comp
from states.states import compitability
from loader import dp, bot
from aiogram import types
from keyboards.inline_keyboards.sovmestimost_kb import compit_kb
from keyboards.inline_keyboards.type_kb import type_kb


@dp.message_handler(commands='sovmestimost')
async def start_sovmestimost(msg: types.Message):
    if compitability.znak_w:
        compitability.znak_w.clear()
    if compitability.znak_m:
        compitability.znak_m.clear()
    await bot.send_message(msg.chat.id, 'Выберите знак девушки', reply_markup=compit_kb)


@dp.callback_query_handler(text_contains='ibt_')
async def znak(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if not compitability.znak_w:
        compitability.znak_w.append(callback_query.data[4:])
        await bot.send_message(callback_query.message.chat.id, 'Выберите знак мужчины', reply_markup=compit_kb)
    else:
        compitability.znak_m.append(callback_query.data[4:])
        await bot.send_message(callback_query.message.chat.id, 'Выберите тип совместимости', reply_markup=type_kb)


@dp.callback_query_handler(text_contains='type_')
async def send_compitability(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    type = call.data[5:]
    v = comp.sovmestimost(compitability.znak_w[0], compitability.znak_m[0], type)
    pred = v[0]
    t = v[1]
    await bot.send_message(call.message.chat.id,
                           f'<b>женщина - {compitability.znak_w[0]}, мужчина - {compitability.znak_m[0]}</b>\n\n' + f'{pred}\n\n<b>{t}</b>\n\n' + '\n'.join(
                               v[2:]), parse_mode='html')
