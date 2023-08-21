import pandas as pd

# Create a DataFrame with categorical variables
data = {'Name': ['John', 'Emily', 'Bob', 'Alice', 'David'],
        'City': ['New York', 'London', 'Paris', 'London', 'Paris'],
        'Salary': [50000, 60000, 55000, 70000, 65000]}
df = pd.DataFrame(data)

# Convert the 'City' column to categorical type
df['City'] = pd.Categorical(df['City'])

# Perform groupby operation on categorical column
grouped_data = df.groupby('City')['Salary'].mean()
print(grouped_data)
