import pandas as pd

data = {'Name': ['John', 'Emma', 'Tom', 'Emily', "North", "Seen"],
        'Age': [25, 28, 23, 27, 38, 38],
        'City': ['New York', 'San Francisco', 'London', 'Paris', 'BKK', 'BKK']}
df = pd.DataFrame(data)


df['Salary'] = [50000, 60000, 45000, 55000, 20000, 30000]  # Add a new column


# print(df['Age'] > 25)  # Boolean filtering
# print(df[df['Age'] > 25])  # Filter rows based on a condition
print(df[(df['Age'] > 25) & (df['City'] == 'New York')])  # Multiple conditions
# print(df.query("Age > 25 and City == 'New York'"))  # Using query method