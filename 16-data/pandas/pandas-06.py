
import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3],
                    'Name': ['John', 'Emma', 'Tom']})
df2 = pd.DataFrame({'ID': [2, 3, 4],
                    'Age': [28, 23, 27]})

# Merge the DataFrames based on a common column
merged_df = pd.merge(df1, df2, on='ID')

print(merged_df)
