import requests

#Задание 2: Параметры запроса

url = "https://jsonplaceholder.typicode.com/posts"

params = {'userId': 1}

response = requests.get(url, params=params)

print("Задание 2:", response.status_code)

for post in response.json():
    print("Задание 2:", post)