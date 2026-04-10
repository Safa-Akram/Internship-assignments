# Assignment: Word Importance Explorer

from sklearn.feature_extraction.text import TfidfVectorizer

# Step 1: Sample documents
documents = [
    "Machine learning is amazing",
    "Artificial intelligence and machine learning",
    "Data science uses machine learning",
    "Deep learning is a part of AI",
    "AI and ML are future technologies"
]

# Step 2: Apply TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# Step 3: Get feature names
features = vectorizer.get_feature_names_out()

# Step 4: Display top words for each document
for i, doc in enumerate(X):
    print(f"\nDocument {i+1} Top Words:")
    scores = zip(features, doc.toarray()[0])
    sorted_words = sorted(scores, key=lambda x: x[1], reverse=True)

    for word, score in sorted_words[:3]:
        print(f"{word} -> {score:.3f}")