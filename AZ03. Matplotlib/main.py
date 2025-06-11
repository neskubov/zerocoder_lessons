import numpy as np
import matplotlib.pyplot as plt

# Гистограмма для нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов
data = np.random.normal(mean, std_dev, num_samples)

# Данные для диаграммы рассеяния
x = np.random.rand(100)  # 100 случайных чисел для оси X
y = np.random.rand(100)  # 100 случайных чисел для оси Y

# Создание полотна для двух графиков
plt.figure(figsize=(10, 5))  # Размер полотна (ширина, высота)

# Первая диаграмма: гистограмма
plt.subplot(1, 2, 1)  # 1 строка, 2 столбца, 1-й график
plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='black')
plt.title("Гистограмма")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.grid(True)

# Вторая диаграмма: диаграмма рассеяния
plt.subplot(1, 2, 2)  # 1 строка, 2 столбца, 2-й график
plt.scatter(x, y, color='green', alpha=0.7)
plt.title("Диаграмма рассеяния")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# Показать оба графика
plt.tight_layout()  # Автоматически отрегулировать расстояние между графиками
plt.show()