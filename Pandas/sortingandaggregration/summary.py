"""
df["Column Name"].min()  # Returns the minimum value in the specified column
df["Column Name"].max()  # Returns the maximum value in the specified column
df["Column Name"].mean()  # Returns the mean (average) value in the specified column
df["Column Name"].median()  # Returns the median value in the specified column
df["Column Name"].sum()  # Returns the sum of all values in the specified column
"""
import pandas as pd

data = {
    "name": ["Alice", "Alex", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"],
    "age": [25, 45, 35, 40, 28, 32, 29, 31],
    "salary": [50000, 35000, 70000, 80000, 55000, 65000, 72000, 58000],
}

df = pd.DataFrame(data)
print("DataFrame created:")
print(df)

print("\nMinimum age:", df["age"].min())
print("Maximum age:", df["age"].max())
print("Mean age:", df["age"].mean())
print("Median age:", df["age"].median())
print("Sum of salaries:", df["salary"].sum())
print("Minimum salary:", df["salary"].min())
print("Maximum salary:", df["salary"].max())
print("Mean salary:", df["salary"].mean())
print("Median salary:", df["salary"].median())
print("Sum of ages:", df["age"].sum())

print("Count :", df["name"].count())