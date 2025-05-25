import requests

#Задание 3: Отправка данных

url = "https://jsonplaceholder.typicode.com/posts"

data = {'title': 'foo', 'body': 'bar', 'userId': 1}

response = requests.post(url, data=data)

print("Задание 3:", response.status_code)
print("Задание 3:", response.json())