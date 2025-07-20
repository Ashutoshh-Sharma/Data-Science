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


# finding missing data
print("\nChecking for missing data:")
print(df.isnull())

# sum is used to count the number of missing values in each column
print(df.isnull().sum())