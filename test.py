import requests

def get_quotes():
    url = "https://quoteslate.vercel.app/api/quotes"  # Предполагаемый API-эндпоинт
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка на ошибки HTTP
        quotes = response.json()  # Преобразование ответа в формат JSON
        return quotes
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None

# Вызов функции и вывод результатов
quotes = get_quotes()
if quotes:
    for quote in quotes:
        print(f'{quote["text"]} - {quote["author"]}')