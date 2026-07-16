import pandas as pd

DATA_PATH = r"C:\ML-Practice-and-Projects\datasets\housing.csv"

# Standard column names for the Boston Housing dataset
BOSTON_COLUMNS = [
    "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS",
    "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"
]

# The CSV does not contain a header row, so we assign the official names manually.
data = pd.read_csv(DATA_PATH, sep=r"\s+", header=None, names=BOSTON_COLUMNS)

print(data.head())
print("\nColumns:", list(data.columns))

print(data.describe())
print(data.isnull().sum())