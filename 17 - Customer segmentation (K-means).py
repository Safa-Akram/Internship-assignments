# Customer Segmentation using K-Means

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dataset
data = {
    "Income": [15,16,17,40,42,20,35,60,65,70],
    "Spending": [39,81,6,77,40,76,6,94,3,14]
}

df = pd.DataFrame(data)

# K-Means
kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(df)

print(df)

# Plot
plt.scatter(df["Income"], df["Spending"], c=df["Cluster"])
plt.xlabel("Income")
plt.ylabel("Spending")
plt.title("Customer Segmentation")
plt.show()