# Assignment 14: Spam Classifier Thinking

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# -------------------------------
# Step 1: Create Sample Dataset
# -------------------------------

messages = [
    "Win a free lottery now",
    "Congratulations you won a prize",
    "Meeting at 10 am tomorrow",
    "Let's have lunch today",
    "Free offer just for you",
    "Project discussion with team"
]

labels = ["Spam", "Spam", "Ham", "Ham", "Spam", "Ham"]

# -------------------------------
# Step 2: Convert text to numbers
# -------------------------------

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# -------------------------------
# Step 3: Train Spam Classifier
# -------------------------------

model = MultinomialNB()
model.fit(X, labels)

# -------------------------------
# Step 4: Test with new message
# -------------------------------

test_message = ["Free gift waiting for you"]

test_vector = vectorizer.transform(test_message)

prediction = model.predict(test_vector)

print("Message:", test_message[0])
print("Prediction:", prediction[0])