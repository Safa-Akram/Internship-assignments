# Student Data Manager

students = {}

# Input data for 5 students
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Calculate class average
total_marks = sum(students.values())
average = total_marks / len(students)

# Find topper
topper = max(students, key=students.get)
top_marks = students[topper]

# Function to assign grade
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

# Display student details with grades
print("\n--- Student Details ---")
for name, marks in students.items():
    grade = assign_grade(marks)
    print(f"Name: {name}, Marks: {marks}, Grade: {grade}")

# Display topper and average
print("\n--- Results ---")
print("Topper:", topper, "with", top_marks, "marks")
print("Class Average:", average)
