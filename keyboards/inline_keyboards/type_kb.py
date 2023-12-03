from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ibt_love = InlineKeyboardButton('Любовь', callback_data='type_Любовь')
ibt_sex = InlineKeyboardButton('🔞Секс🔞', callback_data='type_Секс')
ibt_family = InlineKeyboardButton('Семья и брак', callback_data='type_Семья и брак')
ibt_frandz = InlineKeyboardButton('Дружба', callback_data='type_Дружба')
ibt_work = InlineKeyboardButton('Работа и бизнес', callback_data='type_Работа и бизнес')
type_kb = InlineKeyboardMarkup().insert(ibt_love).insert(ibt_sex).insert(ibt_family).insert(ibt_frandz).insert(ibt_work)
