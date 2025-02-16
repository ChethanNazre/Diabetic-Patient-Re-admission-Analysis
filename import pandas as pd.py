import pandas as pd

# Load the CSV file
train_v = pd.read_csv('modified_diabetes1205_beforeEDA.csv')

# Check the first few rows of the DataFrame
print(train_v.head())

print(train_v.columns)
