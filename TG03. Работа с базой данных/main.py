import aiohttp
import asyncio
import logging
import sqlite3
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from config_bot import TOKEN

bot = Bot(token=TOKEN)
storage_school = MemoryStorage()
dp = Dispatcher(storage=storage_school)
logging.basicConfig(level=logging.INFO)


def create_school_db():
    """Создание таблицы студентов, если её ещё нет"""
    try:
        conn = sqlite3.connect('school_data.db')
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade TEXT NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        logging.error(f"Ошибка при создании базы данных: {e}")
    finally:
        conn.close()


create_school_db()


class StatesGroupSchool(StatesGroup):
    name = State()
    age = State()
    grade = State()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Этот бот регистрирует студентов в базе данных.\nДля регистрации введите команду /registration")


@dp.message(Command('registration'))
async def start_registration(message: Message, state: FSMContext):
    await message.answer("Как тебя зовут?")
    await state.set_state(StatesGroupSchool.name)


@dp.message(StatesGroupSchool.name)
async def set_state_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Сколько тебе лет?")
    await state.set_state(StatesGroupSchool.age)


@dp.message(StatesGroupSchool.age)
async def set_state_age(message: Message, state: FSMContext):
    # Проверка на число
    if not message.text.isdigit():
        await message.answer("Возраст должен быть числом! Попробуй ещё раз.")
        return
    await state.update_data(age=int(message.text))
    await message.answer("В каком классе ты учишься?")
    await state.set_state(StatesGroupSchool.grade)


@dp.message(StatesGroupSchool.grade)
async def set_state_grade(message: Message, state: FSMContext):
    await state.update_data(grade=message.text)
    student_data = await state.get_data()

    try:
        conn = sqlite3.connect('school_data.db')
        cur = conn.cursor()
        cur.execute(
            '''INSERT INTO students (name, age, grade) VALUES (?, ?, ?)''',
            (student_data['name'], student_data['age'], student_data['grade'])
        )
        conn.commit()
        await message.answer("✅ Поздравляю, регистрация в школе успешно завершена!")
    except sqlite3.Error as e:
        logging.error(f"Ошибка при записи в базу данных: {e}")
        await message.answer("❌ Ошибка при сохранении данных. Попробуйте позже.")
    finally:
        conn.close()


async def main():
    try:
        await dp.start_polling(bot)
    except aiohttp.ClientError as e:
        logging.error(f"Ошибка сети: {e}")
    except Exception as e:
        logging.error(f"Неизвестная ошибка: {e}")


if __name__ == '__main__':  # исправлено условие
    asyncio.run(main())