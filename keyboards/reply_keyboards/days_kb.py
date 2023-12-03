from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_today = KeyboardButton('\U00002064Сегодня\U00002064')
button_tomorrow = KeyboardButton('\U00002064Завтра\U00002064')
button_tomorrow02 = KeyboardButton('\U00002064Послезавтра\U00002064')

days_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(button_today, button_tomorrow,
                                                                                button_tomorrow02)
