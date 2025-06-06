import pandas as pd
import numpy as np

subjects = ["Math", "Physics", "Chemistry", "Biology", "English"]
students = ['Вася','Петя','Вова','Женя','Оля','Таня','Леля','Маша','Олег','Шрек']
np.random.seed(42)
grades = np.random.randint(1, 6, size=(10, 5))

df = pd.DataFrame(grades, index=students, columns=subjects)

print(df.head())
print('======================')

print(df.mean())
print('======================')

print(df.median())
print('======================')

print(df.std())
print('======================')

Q1_math = df['Math'].quantile(0.25)
print(Q1_math)
print('======================')

Q3_math = df['Math'].quantile(0.75)
print(Q3_math)
print('======================')

IQR = Q3_math - Q1_math
print(IQR)
print('======================')

