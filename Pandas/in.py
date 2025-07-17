import pandas as pd

# df = pd.read_json("sample_Data.json")

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print("DataFrame created:")
print(df)

print("Information about the DataFrame:")
print(df.info())