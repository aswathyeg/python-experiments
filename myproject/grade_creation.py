
grades = {
    "Anu": 95,
    "Bala": 82,
    "Chitra": 68,
    "Deepak": 74,
    "Esha": 59
}
high_grade = 0
for name, mark in grades.items():
    if mark >= 90:
        grade = 'A'
    elif mark >= 80:
        grade = 'B'
    elif mark >= 70:
        grade = 'C'
    elif mark >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"{name} got grade: {grade}")

    if grade in ['A', 'B']:
        high_grade += 1
    print(f"High grades:{high_grade}")
