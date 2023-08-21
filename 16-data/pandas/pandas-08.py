import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emily', 'Bob', 'Alice', 'David'],
        'Age': [25, 30, 35, 40, 45]}
df = pd.DataFrame(data)

# Define a function to categorize age
def categorize_age(age):
    if age < 30:
        return 'Young'
    elif age < 40:
        return 'Middle-aged'
    else:
        return 'Old'

# Apply the function to create a new column 'Age Category'
df['Age Category'] = df['Age'].apply(categorize_age)

print(df)