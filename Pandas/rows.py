import pandas as pd

df = pd.read_csv("sales_data_Sample.csv", encoding='latin1')

# Print the first few rows of the DataFrame if we don't pass any parameters then it will print the first 5 rows
print(df.head())
print(df.head(10))

# Print the last few rows of the DataFrame if we don't pass any parameters then it will print the first 5 rows
print(df.tail())
print(df.tail(10))