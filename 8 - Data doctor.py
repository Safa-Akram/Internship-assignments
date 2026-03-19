import pandas as pd

# -------------------------------
# Step 1: Create Sample Dataset
# -------------------------------

data = {
    "Name": ["Safa", "Akram", "safa", "John", None, "Akram"],
    "Age": [21, 22, 21, None, 23, 22],
    "City": ["Mysore", "Bangalore", "mysore", "Delhi", "Delhi", "Bangalore"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# -------------------------------
# Step 2: Check Missing Values
# -------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------------
# Step 3: Handle Missing Values
# -------------------------------

# Fill missing Age with mean
df["Age"].fillna(df["Age"].mean(), inplace=True)

# Drop rows where Name is missing
df.dropna(subset=["Name"], inplace=True)

print("\nAfter Handling Missing Values:")
print(df)

# -------------------------------
# Step 4: Remove Duplicates
# -------------------------------

df.drop_duplicates(inplace=True)

print("\nAfter Removing Duplicates:")
print(df)

# -------------------------------
# Step 5: Standardize Text
# -------------------------------

df["Name"] = df["Name"].str.lower()
df["City"] = df["City"].str.lower()

print("\nAfter Standardizing Text:")
print(df)

# -------------------------------
# Final Cleaned Dataset
# -------------------------------

print("\nFinal Cleaned Dataset:")
print(df)

# -------------------------------
# Explanation
# -------------------------------

print("\nWhy Data Cleaning Matters:")
print("1. Improves accuracy of analysis.")
print("2. Removes duplicate records.")
print("3. Ensures consistent formatting.")
print("4. Prevents wrong conclusions.")
print("5. Clean data leads to better decision making.")