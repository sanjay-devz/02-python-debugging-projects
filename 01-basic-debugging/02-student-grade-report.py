students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91,
    "David": 68
}

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"

def display_results(data):
    for name, marks in data.items():
        grade = calculate_grade(marks)
        print(name, "-", marks, "-", grade)

display_results(students)

average = sum(students.values()) / len(students)
print("\nAverage Marks:", average)

highest = max(students, key=students.get)
print("Top Student:", highest, "-", students[highest])

students["Eva"] = 88

print("\nUpdated Results:")
display_results(students)