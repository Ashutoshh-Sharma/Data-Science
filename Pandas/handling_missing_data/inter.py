import pandas as pd

data = {
    "name": ["Alice", "Alex", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"],
    "age": [25, None, 35, 40, 28, 32, 29, 31],
    "salary": [50000, None, 70000, 80000, 55000, 65000, 72000, 58000],
    "Performance Score": [88, None, 85, 90, 87, 93, 89, 91]
}

df = pd.DataFrame(data)
print("DataFrame created:") 
print(df)

# linear, polynomial, time

# df.interpolate(method="linear", inplace=True)  # Linear interpolation for missing values
# print("\nDataFrame after linear interpolation:")
# print(df)

df.interpolate(method="polynomial", order=2, inplace=True)  # Polynomial interpolation for missing values
print("\nDataFrame after polynomial interpolation:")   
print(df)


"""
1- Time series Data - stock prices, temperature readings, etc.
2- numerical data - sales figures, financial data, etc.
3- avoid dropping rows or columns with missing values
"""