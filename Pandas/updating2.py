# Updating columns in a DataFrame
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

df["salary"] = df["salary"] * 1.05  # Increase all salaries by 10%
print("\nDataFrame after increasing all salaries by 10%:")  
print(df)

