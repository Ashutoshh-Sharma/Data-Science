# sorting data
# sorting data 1 column sort_values()
# df.sort_values(by="Columnname", true(Ascending)/false(descending), inplace=True) # sort by column name

import pandas as pd
data = {
    "name": ["Alice", "Alex", "Charlie"],
    "age": [25, 45, 35],
    "salary": [50000, 35000, 70000],
}

df = pd.DataFrame(data)
print("Before sorting:")
print(df)

# df.sort_values(by="age", ascending=True, inplace=True)  # Sort by age in ascending order
# print("DataFrame sorted by age in ascending order:")
# print(df)

df.sort_values(by=["age","salary"], ascending=[True,False], inplace=True)  # Sort by multiple columns in ascending order
print("\nDataFrame sorted by multiple columns in ascending order:") 
print(df)