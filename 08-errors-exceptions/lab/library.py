import pandas as pd

try:
    df = pd.read_csv('data.csv')
    print(df.head())
except pd.errors.ParserError:
    print("Error while parsing CSV.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
