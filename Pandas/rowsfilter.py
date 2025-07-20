import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"],
    "age": [25, 30, 35, 40, 28, 32, 29, 31],
    "salary": [50000, 60000, 70000, 80000, 55000, 65000, 72000, 58000],
    "Performance Score": [88, 92, 85, 90, 87, 93, 89, 91]
}

df = pd.DataFrame(data)
print("DataFrame created:")
print(df)

print("\nFiltering rows where age is greater than 30:")
print(df[df["age"] > 30])

print("\nMultiple conditions: Filtering rows where age is greater than 30 and salary is less than 70000:")
print(df[(df["age"] > 30) & (df["salary"] < 70000)])

print("\nMultiple conditions with OR: Filtering rows where age is less than 30 or salary is greater than 60000:")
print(df[(df["age"] < 30) | (df["salary"] > 60000)])

