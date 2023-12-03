from aiogram import Bot, Dispatcher, types
from aiohttp import web
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
storage = MemoryStorage()
bot = Bot(token=bot_token, parse_mode=types.ParseMode.HTML)
Bot.set_current(bot)
dp = Dispatcher(bot, storage=storage)
app = web.Application()

webhook_path = f'/{bot_token}'
