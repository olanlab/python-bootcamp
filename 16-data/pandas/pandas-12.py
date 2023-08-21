import pandas as pd

# Create a DataFrame with datetime values
data = {'Timestamp': ['2023-01-01 08:30:00', '2023-01-02 12:15:00', '2023-01-03 16:45:00'],
        'Value': [10, 20, 15]}
df = pd.DataFrame(data)

# Convert the 'Timestamp' column to datetime type
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Extract the hour from the datetime column
df['Hour'] = df['Timestamp'].dt.hour

print(df)