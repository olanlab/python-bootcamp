import pandas as pd

data = {'Name': ['John', 'Emma', 'Tom', 'Emily', "North", "Seen"],
        'Age': [25, 28, 23, 27, 38, 38],
        'City': ['New York', 'San Francisco', 'London', 'Paris', 'BKK', 'BKK']}
df = pd.DataFrame(data)

df['Salary'] = [50000, 60000, 45000, 55000, 20000, 30000]  # Add a new column
# df.drop('Salary', axis=1, inplace=True)  # Remove a column
print(df)

# Dictionary
dict = df.to_dict() 
print(dict)

# List
list = df['Salary'].to_list()
print(list)

# Json
json = df.to_json()
print(json)

# Html
html = df.to_html()
print(html)

# Csv
df.to_csv('output.csv', index=False)