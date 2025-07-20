#fillna() is used to fill missing values in a DataFrame.
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

# df.fillna(0, inplace=True) # This will fill all missing values with 0
# print("\nDataFrame after filling missing values with 0:")
# print(df)

df["age"].fillna(df["age"].mean(), inplace=True)  # Fill missing 'age' with the mean age
df["salary"].fillna(df["salary"].mean(), inplace=True)  # Fill missing 'salary' with the mean salary
df["Performance Score"].fillna(df["Performance Score"].mean(), inplace=True)  # Fill missing 'performance   score' with the mean performance score

print("\nDataFrame after filling missing values with mean:")
print(df)