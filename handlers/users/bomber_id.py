import asyncio
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from states.states import Bomber, ID
from loader import dp, bot
from aiogram import types


@dp.message_handler(commands=['bomber'], state='*')
async def pre(msg: types.Message):
    await Bomber.bomb.set()
    await bot.send_message(msg.chat.id, 'Через пробел напишите:\n'
                                        'количество сообщений, для отправки\n'
                                        'id пользователя которому нужно отправить сообщения\n'
                                        'количество секунд задержки между сообщениями (целое число, можно 0)'
                                        '\nсообщение которое нужно отправить')
    await bot.send_message(msg.chat.id, 'Для выхода напишите:\nВыход', reply_markup=
    types.ReplyKeyboardMarkup(resize_keyboard=True).row(types.KeyboardButton('Выход')))
    print(msg.from_user.id)


@dp.message_handler(Text(equals='Выход'), state=Bomber.bomb)
async def ex(msg: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(msg.chat.id, 'Обращайся', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=Bomber.bomb)
async def good(msg: types.Message, state: FSMContext):
    data = msg.text.split()
    st = ' '.join(data[3:])
    try:
        if int(data[1]) == 1090101751:
          await bot.send_message(msg.chat.id, 'Хо Хо Хо, NOOOUP', reply_markup=types.ReplyKeyboardRemove())
          await state.finish()
          return
        await bot.send_message(msg.chat.id, 'Процесс начался...')
        for _ in range(int(data[0])):
            await bot.send_message(int(data[1]), st)
            await asyncio.sleep(int(data[2]))
        await state.finish()
        await bot.send_message(msg.chat.id, 'Успешно')
    except:
        await bot.send_message(msg.chat.id, 'Oops, something went wrong, try again',
                               reply_markup=types.ReplyKeyboardRemove())
        await state.finish()


@dp.message_handler(commands=['id'], state='*')
async def know_id(msg: types.Message):
    await bot.send_message(msg.chat.id, 'Перешли мне сообщение пользователя id которого хочешь узнать')
    await bot.send_message(msg.chat.id, f'Ваш id:\n{msg.from_user.id}')
    await bot.send_message(msg.chat.id, 'Для выхода напиши:\nОтмена')
    await ID.id.set()


@dp.message_handler(Text(equals='Отмена'), state=ID.id)
async def ex(msg: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(msg.chat.id, 'Обращайся')


@dp.message_handler(state=ID.id)
async def get_id(msg: types.Message, state: FSMContext):
    try:
        ident = msg.forward_from.id
        await bot.send_message(msg.chat.id, f'id пользователя:\n{ident}')
        await state.finish()

    except:
        await bot.send_message(msg.chat.id, 'Oops, something went wrong, try again')
        await state.finish()