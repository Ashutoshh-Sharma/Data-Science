import pandas as pd

# Read the CSV file with the specified encoding
# df = pd.read_csv("sales_data_Sample.csv", encoding='latin1')

# Read the excel file with the specified encoding
# df = pd.read_excel("SampleSuperstore.xlsx")

# Read the JSON file with the specified encoding
df = pd.read_json("sample_Data.json")
print(df)

# gcfs -> library used to read data from Google Cloud Storage