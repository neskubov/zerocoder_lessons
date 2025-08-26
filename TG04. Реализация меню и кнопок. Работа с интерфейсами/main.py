import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv
from keyboard import keyboard_main

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
logging.basicConfig(level=logging.INFO)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Hi',reply_markup=keyboard_main)


@dp.message()
async def handle_message(message: Message):
    user = message.from_user
    first_name = user.first_name
    if message.text in ["Привет", "До свидания"]:
        await message.answer(f'{message.text}, {first_name}!')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

