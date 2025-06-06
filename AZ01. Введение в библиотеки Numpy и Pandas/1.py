import pandas as pd

df = pd.read_csv('World-happiness-report-2024.csv')

print(df.head(5))
print('===============================================================')
print(df.info())
print('===============================================================')
print(df.describe())

