import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('.\divanParsWriteTosSqllite\divanParsWriteTosSqllite\scrapy_data.db')
cursor = conn.cursor()

query = "SELECT price FROM items;"
cursor.execute(query)

data = cursor.fetchall()

x_data = [int(item[0].replace(" ", "")) for item in data]

plt.hist(x_data)
plt.title('Пример графика из SQLite3', fontsize=16)
plt.xlabel('X-ось', fontsize=8)
plt.ylabel('Y-ось', fontsize=8)
plt.legend()
plt.grid(True)
plt.xticks(rotation=90, ha='right')

plt.show()

# Закрытие соединения с базой данных
conn.close()