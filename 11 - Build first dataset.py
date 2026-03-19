import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# -------------------------------
# Step 1: Create Dataset
# -------------------------------

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -------------------------------
# Step 2: Identify Features & Label
# -------------------------------

X = df[["Study_Hours"]]   # Feature (Input)
y = df["Marks"]           # Label (Output)

print("\nFeature (X):")
print(X)

print("\nLabel (y):")
print(y)

# -------------------------------
# Step 3: Train Simple ML Model
# -------------------------------

model = LinearRegression()
model.fit(X, y)

# Predict marks for 9 study hours
predicted_marks = model.predict([[9]])

print("\nPredicted Marks for 9 Study Hours:", predicted_marks[0])

# -------------------------------
# Step 4: Visualize Relationship
# -------------------------------

plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

# -------------------------------
# Step 5: Relationship Explanation
# -------------------------------

print("\nRelationship:")
print("There is a positive linear relationship between Study Hours and Marks.")
print("As study hours increase, marks also increase.")