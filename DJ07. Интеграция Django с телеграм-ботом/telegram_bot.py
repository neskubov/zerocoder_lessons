import telebot
from telebot.types import Message
import requests

TOKEN = "TOKEN"
API_URL = "http://127.0.0.1:8000/api"  # эндпоинт Django

bot = telebot.TeleBot(TOKEN)

# Словарь для хранения шагов регистрации
user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Давай зарегистрируемся.\nВведи свой username:")
    user_data[message.chat.id] = {"step": "username"}


@bot.message_handler(func=lambda m: True)
def handle_message(message):
    chat_id = message.chat.id
    if chat_id not in user_data:
        bot.send_message(chat_id, "Нажми /start чтобы начать регистрацию.")
        return

    step = user_data[chat_id]["step"]

    if step == "username":
        user_data[chat_id]["username"] = message.text

        # Отправляем данные в Django
        payload = {
            "user_name": user_data[chat_id]["username"],
            "user_id": message.from_user.id
        }

        try:
            response = requests.post(API_URL + "/register", json=payload)
            data = response.json()
            if response.status_code == 201:
                bot.send_message(chat_id, f"Регистрация прошла успешно! ID: {data['user_id']}")
            elif response.status_code == 200:
                bot.send_message(chat_id, f"Пользователь {data['user_name']} ({data['user_id']}) зарегистрирован ранее")
            else:
                bot.send_message(chat_id, f"Ошибка: {data.get('message', 'Неизвестная ошибка')}")
        except Exception as e:
            bot.send_message(chat_id, f"Ошибка при подключении к серверу: {e}")

        # Очистка
        user_data.pop(chat_id, None)


@bot.message_handler(commands=['myinfo'])
def user_info(message: Message):
    try:
        response = requests.get(f"{API_URL}/user/{message.from_user.id}")
        if response.status_code == 200:
            try:
                data = response.json()
                bot.reply_to(message, f"Ваша регистрация:\n\n{data}")
            except ValueError:
                bot.send_message(message.chat.id, "Ошибка: сервер вернул не JSON")
        elif response.status_code == 404:
            bot.send_message(message.chat.id, "Вы не зарегистрированы!")
        else:
            bot.send_message(message.chat.id, "Непредвиденная ошибка!")
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка подключения к API: {e}")

if __name__ == "__main__":
    bot.polling(none_stop=True)