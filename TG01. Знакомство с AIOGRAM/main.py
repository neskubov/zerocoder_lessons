from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config_bot import TOKEN, WEATHER_CODES

import asyncio
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello world! Введите команду /help")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help\n/weather_moscow")

@dp.message(Command('weather_moscow'))
async def weather_moscow(message: Message):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 55.75,  # Москва
        "longitude": 37.62,
        "current_weather": "true",
        "timezone": "auto"
    }

    response = requests.get(url, params=params)
    data = response.json()

    temperature_scale = data["current_weather_units"]["temperature"]  # шкала температуры ("C" = Celsius, "F" = Fahrenheit)
    temperature_value = data["current_weather"]["temperature"]  # значение температуры
    precipitation = WEATHER_CODES[str(data["current_weather"]["weathercode"])]  # осадки

    await message.answer(f'В Москве: {temperature_value} {temperature_scale}; {precipitation}')

@dp.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять' \
                         'творческие функции, которые традиционно считаются прерогативой человека; наука и технология' \
                         'создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())