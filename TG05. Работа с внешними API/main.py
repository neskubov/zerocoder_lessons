import asyncio
import os
import random
import requests
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from keyboard import menu_start, ChoiceMenu, ChoiceMenuWithAnswer
from config_game import BREEDS, TRUE_ANSWERS_CONGRATULATIONS, WRONG_ANSWER_CONGRATULATIONS


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
storage_dogs = MemoryStorage()
dp = Dispatcher(storage=storage_dogs)
router = Router()


def download_random_image(breed):
    api_url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        image_url = data["message"]

        img_response = requests.get(image_url)
        if img_response.status_code == 200:
            return image_url
    return False


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет, давай поиграем?\nПопробуй угадать породу собаки\n\nЖми «старт»!",
        reply_markup=menu_start
    )


@dp.message(F.text == "Старт")
async def get_image(message: Message):
    global correct_breed_en, correct_breed_ru
    random_breed_keys = random.sample(list(BREEDS.keys()), 4)
    breed_options = {breed: BREEDS[breed] for breed in random_breed_keys}
    correct_breed_en = random.choice(list(breed_options.keys()))
    correct_breed_ru = breed_options[correct_breed_en]
    choice_menu = ChoiceMenu(**breed_options).create()

    image_url = download_random_image(correct_breed_en)
    if image_url:
        await message.answer_photo(photo=image_url, reply_markup=choice_menu)
    else:
        await message.answer("Сервис получения картинок недоступен, попробуйте позже")


@router.callback_query()
async def process_callback(callback: CallbackQuery):
    data = callback.data
    await callback.answer()  # убираем "часики"

    keyboard = callback.message.reply_markup.inline_keyboard
    choice_menu_with_answer = ChoiceMenuWithAnswer(keyboard, correct_breed_en)
    new_markup = choice_menu_with_answer.create(chosen_answer=data)

    await callback.message.edit_reply_markup(reply_markup=new_markup)

    if data == correct_breed_en:
        result = random.choice(TRUE_ANSWERS_CONGRATULATIONS)
    else:
        result = random.choice(WRONG_ANSWER_CONGRATULATIONS)

    await callback.message.answer(result)


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())