#Assignment 15: Customer Segmentation


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# -------------------------------
# Step 1: Create Sample Mall Dataset
# -------------------------------

data = {
    "Customer_ID": [1,2,3,4,5,6,7,8,9,10],
    "Age": [19,22,20,35,40,23,31,45,52,48],
    "Annual_Income": [15,16,17,40,42,20,35,60,65,70],
    "Spending_Score": [39,81,6,77,40,76,6,94,3,14]
}

df = pd.DataFrame(data)

print("Customer Dataset:")
print(df)

# -------------------------------
# Step 2: Select Features
# -------------------------------

X = df[["Annual_Income","Spending_Score"]]

# -------------------------------
# Step 3: Apply K-Means
# -------------------------------

kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(X)

print("\nClustered Data:")
print(df)

# -------------------------------
# Step 4: Visualization
# -------------------------------

plt.scatter(df["Annual_Income"], df["Spending_Score"], c=df["Cluster"])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.show()

# -------------------------------
# Step 5: Customer Groups
# -------------------------------

print("\nCustomer Groups:")
print("Cluster 0 → Medium income, medium spending")
print("Cluster 1 → High income, high spending (Premium customers)")
print("Cluster 2 → Low income, low spending (Budget customers)")