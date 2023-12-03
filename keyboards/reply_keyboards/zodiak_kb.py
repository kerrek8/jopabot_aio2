from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bt_telec = KeyboardButton('\U00002649')
bt_oven = KeyboardButton('\U00002648')
bt_vesy = KeyboardButton('\U0000264E')
bt_kozerog = KeyboardButton('\U00002651')

zodiak_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(bt_telec, bt_oven,
                                                                                  bt_vesy, bt_kozerog)