# Smart Input Program

# Taking user inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Categorizing age
if age < 13:
    category = "Child"
elif age >= 13 and age <= 19:
    category = "Teenager"
elif age >= 20 and age <= 59:
    category = "Adult"
else:
    category = "Senior Citizen"

# Printing personalized message
print("\n--- Personalized Message ---")
print(f"Hello {name}!")
print(f"You are categorized as a {category}.")
print(f"It is great that you enjoy {hobby}!")
