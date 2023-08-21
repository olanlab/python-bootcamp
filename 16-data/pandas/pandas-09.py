import pandas as pd

# Sample data
data = {
    'date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'city': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'temperature': [32, 75, 30, 72],
    'humidity': [80, 60, 85, 40]
}

df = pd.DataFrame(data)
print(df)
print('----------------------------')
# Reshape using pivot
pivot_df = df.pivot(index='date', columns='city')

print("Pivoted DataFrame:")
print(pivot_df)
print('----------------------------')

# Reshape using melt
melted_df = pd.melt(df, id_vars='date', value_vars=['temperature', 'humidity'], var_name='variable', value_name='value')

print("\nMelted DataFrame:")
print(melted_df)
