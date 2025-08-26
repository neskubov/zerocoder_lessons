import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery
from dotenv import load_dotenv
from keyboard import menu_start, menu_multimedia, dynamic_menu, menu_options

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
logging.basicConfig(level=logging.INFO)


@dp.message(CommandStart())
async def command_start(message: Message):
    await message.answer('Это учебный проект: "Работа с интерфесами в телеграм"\n'
                         'Введите /help для получения списка команд',
                         reply_markup=menu_start)


@dp.message(Command('help'))
async def command_help(message: Message):
    await message.answer(
                        '/start - Запуск бота и стартовой клавиатуры\n'
                        '/help - Справка по командам\n'
                        '/links - Меню мультимедиа\n'
                        '/dynamic - Динамическое меню'
                        )


@dp.message(Command('links'))
async def get_menu_multimedia(message: Message):
    await message.answer('Выбери раздел:', reply_markup=menu_multimedia)


@dp.message(Command('dynamic'))
async def get_dynamic_menu(message: Message):
    await message.answer('Динамическое меню',reply_markup=dynamic_menu)


@dp.callback_query(F.data == 'show_more')
async def get_menu_options(callback: CallbackQuery):
    await callback.message.edit_text('Выбери опцию', reply_markup=menu_options)


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

