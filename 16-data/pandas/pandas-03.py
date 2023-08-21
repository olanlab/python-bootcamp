import pandas as pd

data = {'Name': ['John', 'Emma', 'Tom', 'Emily', "North", "Seen"],
        'Age': [25, 28, 23, 27, 38, 38],
        'City': ['New York', 'San Francisco', 'London', 'Paris', 'BKK', 'BKK']}
df = pd.DataFrame(data)


df['Salary'] = [50000, 60000, 45000, 55000, 20000, 30000]  # Add a new column


# print(df['Name'])  # Access a specific column
# print(df['Age'].mean())  # Calculate the mean of a column
# print(df['City'].unique())  # Get unique values in a column
# print(df['Age'].apply(lambda x: x + 1))  # Apply a function to a column
