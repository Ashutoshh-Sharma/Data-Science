import pandas as pd
import numpy as np 

df = pd.read_excel('E:\Learn\Jupyter\Indian_Employee_Data\indian_employees_data.xlsx')
print(df.head())

# Find missing values
print(df.isnull().sum())

# Replace inf and -inf with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill missing values with the mean for numerical columns
df['Salary (INR)'].fillna(df['Salary (INR)'].mean(), inplace=True)
df['Performance Rating'].fillna(df['Performance Rating'].median(), inplace=True)
df['Experience (Years)'].fillna(df['Experience (Years)'].mean(), inplace=True)

print(df.head())


print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Replace negative salaries with the mean salary
df['Salary (INR)'] = np.where(df['Salary (INR)'] < 0, df['Salary (INR)'].mean(), df['Salary (INR)'])

print(df)

salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

# Remove outliers in Salary
# Remove rows where salary is too high or too low
df = df[(df['Salary (INR)'] >= lower_bound) & (df['Salary (INR)'] <= upper_bound)]

# save the cleaned data to a new Excel file
df.to_excel('E:\Learn\Jupyter\Indian_Employee_Data\cleaned_indian_employees_data.xlsx', index=False)

print("Data cleaning complete. Cleaned data saved to 'cleaned_indian_employees_data.xlsx'.")