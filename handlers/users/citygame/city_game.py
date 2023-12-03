from loader import dp, bot
from aiogram import types
import json
from aiogram.dispatcher import FSMContext
from states.states import CityGameState
from aiogram.dispatcher.filters import Text

cities = json.load(open('handlers/users/citygame/only_cities.json', encoding='utf-8'))
used_cities = []
last_b = ['a']


@dp.message_handler(commands=['city_game'], state='*')
async def city_game(message: types.Message):
    last_b.append('1')
    await CityGameState.citygamestate.set()
    await bot.send_message(message.chat.id, 'Назовите любой город',
                           reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).row(
                               types.KeyboardButton('Подсказка')).row(
                               types.KeyboardButton('Отмена')))


@dp.message_handler(Text(equals='Подсказка'), state=CityGameState.citygamestate)
async def help_city_game(message: types.Message, state: FSMContext):
    try:
        for i in cities[last_b[-1]]:
            if i not in used_cities:
                await bot.send_message(message.chat.id, 'попробуй: ' + f'<b>{i}</b>', parse_mode='html')
                break
            else:
                await bot.send_message(message.chat.id,
                                       'Похоже городов на эту букву не осталось...\n' + 'Ты проиграл получается\n' +
                                       'Чтобы выйти из игры, нажми, или напиши <b>отмена</b>',
                                       parse_mode='html')
                break
    except:
        await bot.send_message(message.chat.id, 'Первый город назови уж сам')


@dp.message_handler(Text(equals='Отмена'), state=CityGameState.citygamestate)
async def cancel_city_game(message: types.Message, state: FSMContext):
    used_cities.clear()
    last_b.clear()
    await state.finish()
    await message.reply('🤡Хаха, я выиграл, БОТ ЁБАНЫЙ🤡', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=CityGameState.citygamestate)
async def city_game_handler(message: types.Message, state: FSMContext):
    city = str(message.text).strip().lower()
    f_b = city[0]
    if last_b[-1] not in 'ёйцукенгшщзхъфывапролджэячсмитьбю':
        last_b.append(f_b)
    a = False
    err = 0
    if f_b not in cities.keys():
        a = False
        err = 2
    elif city not in cities[f_b]:
        a = False
        err = 3
    elif city in used_cities:
        a = False
        err = 4
    elif f_b != last_b[-1]:
        a = False
        err = 5
    else:
        a = True
    if a:
        used_cities.append(city)
        l_b = -1
        while True:
            if city[l_b] not in cities.keys():
                l_b -= 1
            else:
                break
        bot_city = 'n'
        for i in cities[city[l_b]]:
            if i not in used_cities:
                bot_city = i
                used_cities.append(i)
                break
        if len(bot_city) != 1:
            post_for_u = -1
            while True:
                if bot_city[post_for_u] not in cities.keys():
                    post_for_u -= 1
                else:
                    break
            last_b.append(bot_city[post_for_u])
            await bot.send_message(message.chat.id, bot_city + '\nВам на букву: ' + bot_city[post_for_u])
        else:
            await state.finish()
            used_cities.clear()
            last_b.clear()
            await bot.send_message(message.chat.id, 'Ты выиграл')
    else:
        if err == 2:
            await bot.send_message(message.chat.id, 'город не может начинаться с такой буквы' + '\nПопробуйте еще раз')
        elif err == 3:
            await bot.send_message(message.chat.id, 'такого города нет' + '\nПопробуйте еще раз')
        elif err == 4:
            await bot.send_message(message.chat.id, 'такой город уже был' + '\nПопробуйте еще раз')
        elif err == 5:
            await bot.send_message(message.chat.id,
                                   'город должен начинаться с последней буквы предыдущего города' + '\nПопробуйте еще раз')
