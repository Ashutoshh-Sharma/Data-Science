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

df["Bonus"] = df["salary"] * 0.1
print("\nDataFrame after adding a new column 'Bonus':")
print(df)

# using insert() to add a column at a specific position

df.insert(0, "Employee ID", range(1, len(df)+1))
print("\nDataFrame after inserting 'Employee ID' at the beginning:")
print(df)
