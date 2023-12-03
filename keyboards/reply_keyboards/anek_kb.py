from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
bt_rand = KeyboardButton('\U00002064Случайный анекдот\U00002064')
bt_prev = KeyboardButton('\U00002064Предыдущий анекдот\U00002064')
bt_next = KeyboardButton('\U00002064Следующий анекдот\U00002064')
bt_anek = KeyboardButton('\U00002064Выход\U00002064')
anek_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(bt_prev, bt_rand, bt_next).add(bt_anek)