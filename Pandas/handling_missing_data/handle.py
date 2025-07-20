# dropna()  remove rows with missing values

import pandas as pd

data = {
    "name": ["Alice", None, "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"],
    "age": [25, None, 35, 40, 28, 32, 29, 31],
    "salary": [50000, None, 70000, 80000, 55000, 65000, 72000, 58000],
    "Performance Score": [88, None, 85, 90, 87, 93, 89, 91]
}

df = pd.DataFrame(data)
print("DataFrame created:") 
print(df)

print("\nDataFrame after dropping rows with any missing values:")
print(df.dropna())

print(df.dropna(inplace=True))  # This will modify the original DataFrame

print(df.dropna(axis=1, inplace=True))  # This will drop columns with any missing values

print(df.dropna(axis=0, inplace=True))  # This will drop rows with any missing values