# Advanced Text Cleaning Program

import string
import re

# Sample text
text = "Heyyy!!! I luv this movie 😍!!!"

# Step 1: Lowercase
text = text.lower()

# Step 2: Remove emojis
text = re.sub(r'[^\w\s]', '', text)  # removes punctuation + emojis

# Step 3: Fix repeated letters (heyyy → hey)
text = re.sub(r'(.)\1+', r'\1', text)

# Step 4: Remove stopwords
stopwords = ["i", "this", "is", "a", "the"]
words = text.split()
cleaned_words = [word for word in words if word not in stopwords]

# Final cleaned text
cleaned_text = " ".join(cleaned_words)

print("Original Text:", "Heyyy!!! I luv this movie 😍!!!")
print("Cleaned Text:", cleaned_text)