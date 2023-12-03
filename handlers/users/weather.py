from loader import dp, bot
from aiogram import types
import json
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from keyboards.reply_keyboards.weather_kbf import weather_kb
import datetime
import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()
weather_API = os.getenv("weather_API")


@dp.message_handler(commands=['weather'])
async def weather(msg: types.Message):
    await bot.send_message(msg.chat.id, 'Выберите интересующую вас опцию', reply_markup=weather_kb)


@dp.message_handler(Text(equals='\U00002063Сейчас\U00002063'))
async def weather_now(msg: types.Message):
    lat = 60.72411
    lon = 77.58138
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_API}&units=metric&lang=ru') as r:
                r = await r.text()
        data = json.loads(r)
        temp = round(data['main']['temp'] + 1)
        feels_like = round(data['main']['feels_like'] + 1)
        wind_speed = data['wind']['speed']
        wind_gust = data['wind']['gust']
        weather = data['weather'][0]['description']
        cloudnes = data['clouds']['all']
        s = f"🌤ПОГОДА СЕЙЧАС🌤\n" \
            f"<b>Температура: {temp}°C</b>\n" \
            f"Ощущается: {feels_like}°C\n" \
            f"Погода: {weather}\n" \
            f"Облачность: {cloudnes}%\n" \
            f"Скорость ветра: {wind_speed}м/с\n" \
            f"Порывы ветра: до {wind_gust}м/с\n"
        await bot.send_message(msg.chat.id, s, parse_mode='html', reply_markup=ReplyKeyboardRemove())

    except Exception as ex:
        print(ex)


@dp.message_handler(Text(equals='\U00002063Сегодня\U00002063'))
async def weather_today(msg: types.Message):
    lat = 60.72411
    lon = 77.58138
    cnt = 8
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt={cnt}&appid={weather_API}&units=metric&lang=ru') as r:
                r = await r.text()
        data = json.loads(r)
        d = data['list']
        s = f'🌤ПОГОДА НА СЕГОДНЯ🌤\n' \
            f'🌤{d[0]["dt_txt"][8:10] + "-" + d[0]["dt_txt"][5:7] + "-" + d[0]["dt_txt"][0:4]}🌤\n'

        spisok_vstavki = []
        for i in range(len(d)):
            if int(d[i]['dt_txt'][11:13]) + 4 == 25:
                break
            h = [str(int(d[i]['dt_txt'][-8:-6]) + 4) + ':00', d[i]['main']['temp'], d[i]['main']['feels_like'],
                 d[i]['weather'][0]['description']]
            spisok_vstavki.append(h)

        for i in spisok_vstavki:
            s = s + f'\nВ {i[0]} \n' + f'<b>Температура: {round(i[1] + 2)}\n</b>' + f'Ощущается как: {round(i[2] + 1)}\n' + f'Погода: {i[3]}\n'
        await bot.send_message(msg.chat.id, s, parse_mode='html', reply_markup=ReplyKeyboardRemove())
    except Exception as ex:
        print(ex)


@dp.message_handler(Text(equals='\U00002063Завтра\U00002063'))
async def weather_today(msg: types.Message):
    lat = 60.72411
    lon = 77.58138
    cnt = 16
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt={cnt}&appid={weather_API}&units=metric&lang=ru') as r:
                r = await r.text()
        data = json.loads(r)
        d = data['list']
        day = datetime.datetime.now().strftime('%d')
        while True:
            if int(d[0]['dt_txt'][8:10]) == int(day):
                del d[0]
            else:
                break

        s = f'🌤ПОГОДА НА ЗАВТРА🌤\n' \
            f'🌤{d[0]["dt_txt"][8:10] + "-" + d[0]["dt_txt"][5:7] + "-" + d[0]["dt_txt"][0:4]}🌤\n'

        spisok_vstavki = []
        for i in range(len(d)):
            if int(d[i]['dt_txt'][11:13]) + 4 == 25:
                break
            h = [str(int(d[i]['dt_txt'][-8:-6]) + 4) + ':00', d[i]['main']['temp'], d[i]['main']['feels_like'],
                 d[i]['weather'][0]['description']]
            spisok_vstavki.append(h)

        for i in spisok_vstavki:
            s = s + f'\nВ {i[0]} \n' + f'<b>Температура: {round(i[1] + 2)}</b>\n' + f'Ощущается как: {round(i[2] + 1)}\n' + f'Погода: {i[3]}\n'
        await bot.send_message(msg.chat.id, s, parse_mode='html', reply_markup=ReplyKeyboardRemove())
    except Exception as ex:
        print(ex)


@dp.message_handler(Text(equals='\U00002063Послезавтра\U00002063'))
async def weather_today(msg: types.Message):
    lat = 60.72411
    lon = 77.58138
    cnt = 35
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt={cnt}&appid={weather_API}&units=metric&lang=ru') as r:
                r = await r.text()
        data = json.loads(r)
        d = data['list']
        day = datetime.datetime.now().strftime('%d')
        while True:
            if int(d[0]['dt_txt'][8:10]) == int(day) or int(d[0]['dt_txt'][8:10]) == (int(day) + 1):
                del d[0]
            else:
                break

        s = f'🌤ПОГОДА НА ПОСЛЕЗАВТРА🌤\n' \
            f'🌤{d[0]["dt_txt"][8:10] + "-" + d[0]["dt_txt"][5:7] + "-" + d[0]["dt_txt"][0:4]}🌤\n'

        spisok_vstavki = []
        for i in range(len(d)):
            if int(d[i]['dt_txt'][11:13]) + 4 == 25:
                break
            h = [str(int(d[i]['dt_txt'][-8:-6]) + 4) + ':00', d[i]['main']['temp'], d[i]['main']['feels_like'],
                 d[i]['weather'][0]['description']]
            spisok_vstavki.append(h)

        for i in spisok_vstavki:
            s = s + f'\nВ {i[0]} \n' + f'<b>Температура: {round(i[1] + 2)}</b>\n' + f'Ощущается как: {round(i[2] + 1)}\n' + f'Погода: {i[3]}\n'
        await bot.send_message(msg.chat.id, s, parse_mode='html', reply_markup=ReplyKeyboardRemove())
    except Exception as ex:
        print(ex)


@dp.message_handler(Text(equals='\U00002063После послезавтра\U00002063'))
async def weather_today(msg: types.Message):
    lat = 60.72411
    lon = 77.58138
    cnt = 40
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt={cnt}&appid={weather_API}&units=metric&lang=ru') as r:
                r = await r.text()
        data = json.loads(r)
        d = data['list']
        day = datetime.datetime.now().strftime('%d')
        while True:
            if int(d[0]['dt_txt'][8:10]) == int(day) or int(d[0]['dt_txt'][8:10]) == (int(day) + 1) or int(
                    d[0]['dt_txt'][8:10]) == (int(day) + 2):
                del d[0]
            else:
                break

        s = f'🌤ПОГОДА НА ПОСЛЕЗАВТРА🌤\n' \
            f'🌤{d[0]["dt_txt"][8:10] + "-" + d[0]["dt_txt"][5:7] + "-" + d[0]["dt_txt"][0:4]}🌤\n'

        spisok_vstavki = []
        for i in range(len(d)):
            if int(d[i]['dt_txt'][11:13]) + 4 == 25:
                break
            h = [str(int(d[i]['dt_txt'][-8:-6]) + 4) + ':00', d[i]['main']['temp'], d[i]['main']['feels_like'],
                 d[i]['weather'][0]['description']]
            spisok_vstavki.append(h)

        for i in spisok_vstavki:
            s = s + f'\nВ {i[0]} \n' + f'<b>Температура: {round(i[1] + 2)}</b>\n' + f'Ощущается как: {round(i[2] + 1)}\n' + f'Погода: {i[3]}\n'
        await bot.send_message(msg.chat.id, s, parse_mode='html', reply_markup=ReplyKeyboardRemove())
    except Exception as ex:
        print(ex)


@dp.message_handler(Text(equals='\U00002063На 5 дней\U00002063'))
async def weather_all(msg: types.Message):
    lat = 60.72411
    lon = 77.58138
    cnt = 40
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt={cnt}&appid={weather_API}&units=metric&lang=ru') as r:
                r = await r.text()
        data = json.loads(r)
        d = data['list']

        s = f'🌤ПОГОДА НА 5 ДНЕЙ🌤\n'

        spisok_vstavki = []
        for i in range(len(d)):
            if int(d[i]['dt_txt'][11:13]) + 4 == 25:
                continue
            h = [f"{str(int(d[i]['dt_txt'][8:10]))}-{str(int(d[i]['dt_txt'][5:7]))}-{str(int(d[i]['dt_txt'][0:4]))}",
                 str(int(d[i]['dt_txt'][-8:-6]) + 4) + ':00',
                 d[i]['main']['temp'], d[i]['main']['feels_like'],
                 d[i]['weather'][0]['description']]
            spisok_vstavki.append(h)

        for i in spisok_vstavki:
            if i[0] in s:
                s = s + f'\nВ {i[1]} \n' + f'<b>Температура: {round(i[2] + 2)}</b>\n' + f'Ощущается как: {round(i[3] + 1)}\n' + f'Погода: {i[4]}\n'
            else:
                s = s + f'\n🌤{i[0]}🌤\n' + f'\nВ {i[1]} \n' + f'<b>Температура: {round(i[2] + 2)}</b>\n' + f'Ощущается как: {round(i[3] + 1)}\n' + f'Погода: {i[4]}\n'
        await bot.send_message(msg.chat.id, s, parse_mode='html', reply_markup=ReplyKeyboardRemove())
    except Exception as ex:
        print(ex)
