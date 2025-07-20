import pandas as pd

data = {
    "name": ["Alice", "Alex", "Charlie", "David", "Eve"],
    "age": [28, 34, 22, 34, 28],
    "salary": [50000, 60000, 45000, 52000, 48000],
}

df = pd.DataFrame(data)
print("DataFrame created:")
print(df)

# print(df.groupby("age")["salary"].sum())  # Group by 'age' and sum 'salary'


print(df.groupby(["age", "name"])["salary"].sum())