from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.states import WaitToCall
from aiogram.dispatcher.filters import Text


@dp.message_handler(commands=['call'])
async def call(msg: types.Message):
    if msg.from_user.id == 1090101751:
        await WaitToCall.callhandlerstate.set()
        await bot.send_message(msg.chat.id, 'отправляй сообщения и я перешлю их в жопу',
                               reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).row(
                                   types.KeyboardButton('\U00002063Отмена')))


@dp.message_handler(Text(equals='\U00002063Отмена'), state=WaitToCall.callhandlerstate)
async def escape(msg: types.Message, state: FSMContext):
    await state.finish()
    await bot.send_message(msg.chat.id, 'обращайся', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=WaitToCall.callhandlerstate)
async def enter(msg: types.Message):
    await bot.send_message(-1001841458995, msg.text)
