from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

new = KeyboardButton('\U00002063Самые последние новости\U00002063')
more = KeyboardButton('\U00002063Ещё\U00002063')
bt_exit = KeyboardButton('\U00002064Выход\U00002064')
news_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(new).row(more).row(bt_exit)