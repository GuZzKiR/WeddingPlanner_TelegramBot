from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton("Открыть Wedding Planner 💍", web_app=types.WebAppInfo(url=WEB_APP_URL))
    keyboard.add(web_app_button)

    await message.answer("Привет! 👋 Нажми кнопку ниже, чтобы открыть планировщик свадьбы:", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp)
