import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Create Sample Dataset
# -------------------------------

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [20000, 25000, 30000, 28000, 35000],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "Customer_Age": [22, 25, 28, 35, 40]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -------------------------------
# Step 2: Bar Chart (Monthly Sales)
# -------------------------------

plt.figure()
plt.bar(df["Month"], df["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.show()

# -------------------------------
# Step 3: Pie Chart (Category Distribution)
# -------------------------------

category_counts = df["Category"].value_counts()

plt.figure()
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
plt.title("Sales Category Distribution")
plt.show()

# -------------------------------
# Step 4: Histogram (Customer Age Distribution)
# -------------------------------

plt.figure()
plt.hist(data["Customer_Age"], bins=5)
plt.xlabel("Customer Age")
plt.ylabel("Frequency")
plt.title("Customer Age Distribution")
plt.show()

# -------------------------------
# Step 5: Short Data Story
# -------------------------------

print("\nData Story:")
print("1. Sales show an overall increasing trend from January to May.")
print("2. Electronics category contributes more to total sales compared to Clothing.")
print("3. Most customers fall in the age group of 25 to 40 years.")
print("4. The business is growing steadily with peak sales in May.")
