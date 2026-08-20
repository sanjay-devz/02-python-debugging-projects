employees = {
    "John": 25000,
    "Emma": 32000,
    "David": 28000,
    "Sophia": 35000
}

def calculate_bonus(salary):
    if salary >= 30000:
        return salary * 10 / 100
    else:
        return salary * 5 / 100

def total_salary(salary):
    return salary + calculate_bonus(salary)

def display_report(data):
    for name, salary in data.items():
        total = total_salary(salary)
        print(name, "-", "Salary:", salary, "Total:", total)

display_report(employees)

highest = max(employees, key=employees.get)
print("\nHighest Paid Employee:", highest)

average = sum(employees.values()) / len(employees)
print("Average Salary:", average)

employees["Liam"] = 29000

print("\nUpdated Employee Report")
display_report(employees)
