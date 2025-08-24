import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command
from config_bot import TOKEN
from googletrans import Translator
from gtts import gTTS

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Этот бот работает с мультимедиа.\nВведите команду /help")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет:\n- сохранять фото\n- переводить русский текст на английский и озвучивать перевод")

@dp.message(F.photo)
async def img(message: Message):
    await bot.download(message.photo[-1], destination=f'img/{message.photo[-1].file_id}.jpg')
    await message.answer(f"Фото успешно сохранено с именем {message.photo[-1].file_id}.jpg")

@dp.message()
async def audio(message: Message):
    try:
        translator = Translator()
        english_text = await translator.translate(message.text.lower(), src="ru", dest="en")  # <--- await
        tts = gTTS(text=english_text.text, lang="en")
        file_path = "audio/result.mp3"
        tts.save(file_path)
        audio = FSInputFile(file_path)
        await bot.send_chat_action(message.chat.id, "upload_voice")
        await message.answer_voice(audio)
    except Exception as e:
        await message.answer(f"Ошибка при обработке текста: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())