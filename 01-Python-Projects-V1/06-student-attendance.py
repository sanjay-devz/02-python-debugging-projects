students = [
    ["Alice", 45, 50],
    ["Bob", 32, 50],
    ["Charlie", 48, 50],
    ["David", 28, 50]
]

def attendance_percentage(attended, total):
    return attended / total * 100

def eligibility(percent):
    if percent >= 75:
        return "Eligible"
    else:
        return "Not Eligible"


def highest_attenance():
    highest = max(students, key=lambda x: x[1])
    print("Best Attendance:", highest[0], "-", highest[1])


def display_report(data):
    for student in data:
        name = student[0]
        attended = student[1]
        total = student[2]

        percent = attendance_percentage(attended, total)
        status = eligibility(percent)

        print(name)
        print(f"Attendance: {percent:.2f}") 
        print("Status:", status)
        print("-" * 25)

display_report(students)
highest_attenance()


students.append(["Eva", 47, 50])

print("\nUpdated Report")
display_report(students)
highest_attenance()