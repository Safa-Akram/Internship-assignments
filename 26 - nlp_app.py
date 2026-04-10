# Simple NLP Mini App - Keyword Extractor

import string

text = input("Enter a sentence: ")

# Step 1: Lowercase
text = text.lower()

# Step 2: Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Step 3: Remove stopwords
stopwords = ["is", "a", "the", "and", "in", "on", "at", "to"]
words = text.split()

keywords = [word for word in words if word not in stopwords]

print("Keywords:", keywords)