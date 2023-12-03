from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ibt_telec = InlineKeyboardButton('♉', callback_data='ibt_telec')
ibt_oven = InlineKeyboardButton('♈', callback_data='ibt_oven')
ibt_vesy = InlineKeyboardButton('♎', callback_data='ibt_vesy')
ibt_kozerog = InlineKeyboardButton('♑', callback_data='ibt_kozerog')
ibt_bliznecy = InlineKeyboardButton('♊', callback_data='ibt_bliznecy')
ibt_rak = InlineKeyboardButton('♋', callback_data='ibt_rak')
ibt_lev = InlineKeyboardButton('♌', callback_data='ibt_lev')
ibt_deva = InlineKeyboardButton('♍', callback_data='ibt_deva')
ibt_skorpion = InlineKeyboardButton('♏', callback_data='ibt_skorpion')
ibt_strelec = InlineKeyboardButton('♐', callback_data='ibt_strelec')
ibt_vodolej = InlineKeyboardButton('♒', callback_data='ibt_vodolej')
ibt_ryby = InlineKeyboardButton('♓', callback_data='ibt_ryby')

compit_kb = InlineKeyboardMarkup().row(ibt_telec, ibt_oven,
                                       ibt_vesy, ibt_kozerog,
                                       ibt_bliznecy, ibt_ryby).row(ibt_rak, ibt_lev,
                                                                   ibt_deva, ibt_skorpion,
                                                                   ibt_strelec, ibt_vodolej)
