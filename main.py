from loader import bot, webhook_path, dp
from background import keep_alive
import handlers
from aiogram.utils.executor import start_webhook
from utils.set_bot_commands import set_default_commands


keep_alive()

WEBHOOK_HOST = 'bestjopabot.kerrek8.repl.co'
WEBHOOK_PATH = f'{webhook_path}'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

#WEBAPPHOST = '0.0.0.0'
#WEBAPPPORT = 80


async def on_startup(dp):
    await set_default_commands(dp)
    # webhook_uri = f'{ngrok_address}{webhook_path}'
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown():
    await bot.delete_webhook()


keep_alive()
if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=webhook_path,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        #host=WEBAPPHOST,
        #port=WEBAPPPORT,
    )
