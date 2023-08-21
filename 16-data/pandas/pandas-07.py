import pandas as pd

data = {'Name': ['John', 'Emma', 'Tom', 'Emily', "North", "Seen"],
        'Age': [None, 28, 23, 27, 38, 38],
        'City': ['New York', 'San Francisco', 'London', "Paris", 'BKK', 'BKK']}
df = pd.DataFrame(data)


print(df.isnull())
print('-----------------------------------')

print(df)
print('-----------------------------------')

df_dropna = df.dropna()
print(df_dropna)
print('-----------------------------------')

df_fillna = df.fillna(0)
print(df_fillna)
print('-----------------------------------')

df_fillna = df.fillna(df.mean())
print(df_fillna)
print('-----------------------------------')
