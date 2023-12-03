from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bt_dice0 = KeyboardButton('\U00002064Кости\U00002064')
bt_dice1 = KeyboardButton('\U00002064Автомат\U00002064')
bt_dice2 = KeyboardButton('\U00002064Дартс\U00002064')
bt_dice3 = KeyboardButton('\U00002064Баскетбол\U00002064')
bt_dice4 = KeyboardButton('\U00002064Футбол\U00002064')
bt_exit = KeyboardButton('\U00002064Выход\U00002064')
games_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(bt_dice0, bt_dice2, bt_dice4).row(bt_dice1, bt_dice3).add(
    bt_exit)
