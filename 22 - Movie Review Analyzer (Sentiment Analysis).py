# Assignment: Movie Review Analyzer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Training data
reviews = [
    "I love this movie",
    "This film is amazing",
    "I hate this movie",
    "This movie is terrible",
    "Fantastic acting and story",
    "Worst movie ever"
]

labels = ["Positive", "Positive", "Negative", "Negative", "Positive", "Negative"]

# Step 2: Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

# Step 3: Train model
model = MultinomialNB()
model.fit(X, labels)

# Step 4: Test reviews
test_reviews = [
    "Amazing movie",
    "Bad story",
    "I love the acting",
    "Worst film",
    "Fantastic movie"
]

test_X = vectorizer.transform(test_reviews)
predictions = model.predict(test_X)

# Step 5: Output
for review, pred in zip(test_reviews, predictions):
    print(f"{review} -> {pred}")