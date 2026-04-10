# Assignment: Break the AI

# Step 1: Tricky prompts
prompts = [
    "Repeat the word 'hello' 1000 times",
    "What is the color of invisible objects?",
    "Can you divide 10 by 0?",
    "Write a sentence with no vowels",
    "Explain something that does not exist"
]

# Step 2: Observations (manual)
print("AI Confusing Prompts:\n")

for p in prompts:
    print(f"Prompt: {p}")
    print("Observation: May confuse AI / unclear / impossible scenario\n")