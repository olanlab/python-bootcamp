import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Emily', 'Bob', 'Alice', 'David', "North"],
        'Age': [25, 30, 35, 40, 45, 38],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney', 'Paris'],
        'Salary': [50000, 60000, 55000, 70000, 65000, 150000]}
df = pd.DataFrame(data)

# Group data by City and calculate average salary
average_salary_by_city = df.groupby('City')['Salary'].mean()
print(average_salary_by_city)