import asyncio
import os
import random
import requests
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from keyboard import menu_start, ChoiceMenu
from config_game import BREEDS, TRUE_ANSWERS_CONGRATULATIONS, WRONG_ANSWER_CONGRATULATIONS


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
storage_dogs = MemoryStorage()
dp = Dispatcher(storage=storage_dogs)
router = Router()


def download_random_image(breed, save_path="random_dog.jpg"):
    api_url = f"https://dog.ceo/api/breed/{breed}/images/random"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        image_url = data["message"]

        img_response = requests.get(image_url)
        if img_response.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(img_response.content)
            print(f"Картинка собаки сохранена в {save_path}")
            return image_url
        else:
            print("Не удалось скачать картинку:", img_response.status_code)
    else:
        print("Не удалось получить ссылку:", response.status_code)



@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, давай поиграем?\nПопробуй угадать породу собаки\n\n Жми «старт»!", reply_markup=menu_start)

@dp.message(F.text == "Старт")
async def get_image(message: Message):
    global correct_breed_en, correct_breed_ru
    random_breed_keys = random.sample(list(BREEDS.keys()), 4)
    breed_options = {breed: BREEDS[breed] for breed in random_breed_keys}
    correct_breed_en = random.choice(list(breed_options.keys()))
    correct_breed_ru = breed_options[correct_breed_en]
    image_url = download_random_image(correct_breed_en)
    choice_menu = ChoiceMenu(**breed_options).create()

    await message.answer_photo(photo=image_url, reply_markup=choice_menu)

@router.callback_query()
async def process_callback(callback: CallbackQuery):
    data = callback.data  # то, что ты положил в callback_data
    await callback.answer()  # ответ, чтобы убрать "часики"
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