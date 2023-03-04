import pandas as pd

# Read the Excel file into a pandas dataframe
df = pd.read_excel('SampleInput.xlsx')

# Convert the dataframe to a JSON string
data = df.to_json(orient='records')