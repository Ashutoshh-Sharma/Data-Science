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

# print("\nSingle column selection (Names): return a Series")
# print(df["name"])

print("\nMultiple columns selection (Name and Salary): return a DataFrame")
print(df[["name", "salary"]])