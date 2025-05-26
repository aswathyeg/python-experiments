updated_salaries = {}
employees = {
    "Alice": 60000,
    "Bob": 45000,
    "Charlie": 52000,
    "Diana": 75000,
    "Eve": 39000
}

for name, salary in employees.items():
    if salary <= 50000:
        bonus = salary * 0.10
        new_salary = salary + bonus
    else:
        new_salary = salary
    updated_salaries[name] = new_salary

print("\nUpdated Salaries Dictionary:")
print(updated_salaries)
