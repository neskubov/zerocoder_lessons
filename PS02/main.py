import requests

#Задание 1: Получение данных

url = "https://api.github.com"

params = {
    'q': 'html'
}

response = requests.get(url, params=params)
print("Задание 1:", response.status_code)
print("Задание 1:", response.json())
print("#############################")


#Задание 2: Параметры запроса

url = "https://jsonplaceholder.typicode.com/posts"

params = {'userId': 1}

response = requests.get(url, params=params)

print("Задание 2:", response.status_code)
print("Задание 2:", response.json())
print("#############################")


#Задание 3: Отправка данных

url = "https://jsonplaceholder.typicode.com/posts"

data = {'title': 'foo', 'body': 'bar', 'userId': 1}

response = requests.post(url, data=data)

print("Задание 3:", response.status_code)
print("Задание 3:", response.json())
print("#############################")