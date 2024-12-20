import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from datetime import datetime

BOT_TOKEN = '8015779574:AAE5cFn7d_jqAxVWpBNzUw6wMayJ462J8EM'
WEATHER_API_KEY = '4bdfbb66f3106af2e781ac3af62ef284'
CITY = 'Samara'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Узнать погоду в Самаре", callback_data="get_weather")]
    ])
    return keyboard


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот погоды для Самары.\n"
        "Нажмите на кнопку ниже, чтобы узнать текущую погоду.",
        reply_markup=get_keyboard()
    )


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = (
        "Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать это сообщение\n"
        "Также вы можете использовать кнопку для получения информации о погоде."
    )
    await message.answer(help_text)


async def get_weather_info():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    try:
        response = requests.get(url)
        data = response.json()

        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']

        weather_text = (
            f"🌡 Температура: {temp}°C\n"
            f"🌤 Погода: {description}\n"
            f"💧 Влажность: {humidity}%\n"
            f"\nОбновлено: {datetime.now().strftime('%H:%M:%S')}"
        )
        return weather_text
    except:
        return "Извините, не удалось получить информацию о погоде."


@dp.callback_query(lambda c: c.data == "get_weather")
async def process_callback_weather(callback_query: types.CallbackQuery):
    await callback_query.answer()
    weather_info = await get_weather_info()
    await callback_query.message.answer(weather_info, reply_markup=get_keyboard())


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())