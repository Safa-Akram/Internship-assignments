# Assignment 12 - KNN in Real Life


from sklearn.neighbors import NearestNeighbors
import pandas as pd

# -------------------------------
# Step 1: Create Sample Dataset
# (Movies with ratings features)
# -------------------------------

data = {
    "Movie": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"],
    "Action": [5, 4, 1, 2, 4],
    "Comedy": [1, 2, 5, 4, 2],
    "Romance": [1, 1, 4, 5, 2]
}

df = pd.DataFrame(data)

print("Movie Dataset:\n")
print(df)

# -------------------------------
# Step 2: Features for similarity
# -------------------------------

features = df[["Action", "Comedy", "Romance"]]

# -------------------------------
# Step 3: Apply KNN
# -------------------------------

knn = NearestNeighbors(n_neighbors=3)
knn.fit(features)

# Find movies similar to Movie A
movie_index = 0
distances, indices = knn.kneighbors([features.iloc[movie_index]])

print("\nMovies similar to:", df.iloc[movie_index]["Movie"])

for i in indices[0][1:]:
    print(df.iloc[i]["Movie"])

# -------------------------------
# Step 4: Explanation
# -------------------------------

print("\nExplanation:")
print("KNN finds similar items based on feature similarity.")
print("Netflix uses similar logic to recommend movies.")
print("If users like a movie, the system recommends movies with similar patterns.")