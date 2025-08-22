import telebot
import requests

TOKEN = "7544393487:AAEfB6Nj4Y9q7xkguZffwkwYsXQTh6gQ7rk"
API_URL = "http://127.0.0.1:8000/api/register"  # эндпоинт Django

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
        user_data[chat_id]["step"] = "user_id"
        bot.send_message(chat_id, "Теперь введи id:")

    elif step == "user_id":
        user_data[chat_id]["user_id"] = message.text

        # Отправляем данные в Django
        payload = {
            "user_name": user_data[chat_id]["username"],
            "user_id": user_data[chat_id]["user_id"]
        }
        print(payload)

        try:
            response = requests.post(API_URL, json=payload)
            print(response)
            print(response.status_code)
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

bot.polling(none_stop=True)