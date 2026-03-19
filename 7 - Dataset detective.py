import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

# Convert to DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Display top 5 rows
print("Top 5 Rows:")
print(df.head())

# Find column with highest maximum value
max_values = df.max()
highest_column = max_values.idxmax()

print("\nColumn with Highest Maximum Value:", highest_column)

# Count missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())