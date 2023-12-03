from loader import dp, bot
from aiogram import types
from datetime import datetime, timedelta


@dp.message_handler(commands='mute')
async def mute(msg: types.Message):
    try:
        admin_list = [admin.user.id for admin in await bot.get_chat_administrators(msg.chat.id)]
        if msg.from_user.id not in admin_list:
            await bot.send_message(msg.chat.id, '😇Могут использовать только администраторы😇')
        elif msg.reply_to_message.from_user.id in admin_list:
            await bot.send_message(msg.chat.id, 'Невозможно замутить администратора')
        else:
            if not msg.reply_to_message:
                await msg.reply("Эта команда должна быть ответом на сообщение!")
                return
            else:
                await bot.restrict_chat_member(msg.chat.id, msg.reply_to_message.from_user.id,
                                               types.ChatPermissions(can_send_messages=False),
                                               until_date=datetime.now() + timedelta(minutes=3))
                await bot.send_message(msg.chat.id, 'иди покакай')
    except Exception as ex:
        print(ex)