import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print(df)
# Save the DataFrame to a CSV file
# df.to_csv("output_data.csv", index=False)  #index=False prevents writing row indices to the file

# df.to_excel("output_data.xlsx", index=False)  # Save to Excel file

df.to_json("output_data.json", index=False)  # Save to JSON file

