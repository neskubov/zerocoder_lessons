import pandas as pd

pd.set_option('display.max_columns', None)

df = pd.read_csv('dz.csv')

result = df.groupby('City')['Salary'].mean()

print(result)
