import requests

#Задание 1: Получение данных

url = "https://api.github.com/search/repositories"

params = {
    'q': 'language:html'
}

response = requests.get(url, params=params)
print("Задание 1:", response.status_code)
print("Задание 1:", response.json())