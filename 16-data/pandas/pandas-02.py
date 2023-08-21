import pandas as pd

data = {'Name': ['John', 'Emma', 'Tom', 'Emily', "North", "Seen"],
        'Age': [25, 28, 23, 27, 38, 38],
        'City': ['New York', 'San Francisco', 'London', 'Paris', 'BKK', 'BKK']}
df = pd.DataFrame(data)


df['Salary'] = [50000, 60000, 45000, 55000, 20000, 30000]  # Add a new column

print(df.head())  # View the first few rows
print(df.info())  # Get information about the DataFrame
print(df.describe())  # Get summary statistics of numeric columns)
