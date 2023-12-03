from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bt_now = KeyboardButton('\U00002063Сейчас\U00002063')
bt_today = KeyboardButton('\U00002063Сегодня\U00002063')
bt_tomorrow = KeyboardButton('\U00002063Завтра\U00002063')
bt_aftertomorrow = KeyboardButton('\U00002063Послезавтра\U00002063')
bt_afteraftertomorrow = KeyboardButton('\U00002063После послезавтра\U00002063')
bt_all = KeyboardButton('\U00002063На 5 дней\U00002063')

weather_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(bt_now).row(bt_today, bt_tomorrow).row(bt_aftertomorrow, bt_afteraftertomorrow).row(bt_all)
