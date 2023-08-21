import pandas as pd

data = {'Name': ['John', 'Emma', 'Tom', 'Emily', "North", "Seen"],
        'Age': [25, 28, 23, 27, 38, 38],
        'City': ['New York', 'San Francisco', 'London', 'Paris', 'BKK', 'BKK']}
df = pd.DataFrame(data)


df['Salary'] = [50000, 60000, 45000, 55000, 20000, 30000]  # Add a new column

grouped_data = df.groupby('City')  # Group data by a column
print(grouped_data['Age'].mean())  # Calculate the mean of a grouped column
print(grouped_data['Salary'].sum())  # Calculate the sum of a grouped column