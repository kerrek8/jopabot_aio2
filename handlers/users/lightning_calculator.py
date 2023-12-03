from loader import dp, bot
from aiogram import types


@dp.message_handler(commands=['lc'])
async def lightning_calculator(message: types.Message):
    try:
        time = message.text.split()[-1]
        await bot.send_message(message.chat.id, f'Молния ударила на расстоянии: <b>{int(time) * 340} метров</b>',
                               parse_mode='html')
    except Exception as ex:
        await bot.send_message(message.chat.id,
                               'неправильный формат ввода\nвведите команду, и через пробел количество секунд прошедшее от вспышки до грома')
