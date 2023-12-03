from loader import dp, bot
from aiogram import types


@dp.message_handler(commands=['kraken'])
async def cat(messenge: types.Message):
    await bot.send_animation(messenge.chat.id,
                             'CgACAgQAAxkBAAIPOmSAB4wG6XhDCtAkGazLbtNLb2EOAAIxAwACypUlUD6x3ccitmmULwQ')

# @dp.message_handler(content_types=['animation'])
# async def get_id(message: types.Message):
#     print(message.animation.file_id)
