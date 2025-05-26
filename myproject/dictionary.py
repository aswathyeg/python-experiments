# 1:
student = {"name": "Deepa", "class": 10, "marks": 87}
print(student["name"])
student["marks"] = 91
print(student["marks"])
del (student["class"])
print(student)

# 2:
fruits = {"apple": 3, "banana": 5, "cherry": 12}

for fruit, quantity in fruits.items():
    print(f"{fruit} has {quantity} items")

 # 3
count = 0
students = {
    "Asha": 88,
    "Bala": 75,
    "Chetan": 92,
    "Diya": 67
}
for student, mark in students.items():
    if mark >= 80:
        print(f"{student}")

    if mark < 70:
        count += 1
        print(f"Number of students sscored less than 70: {count} ")

# 4
peoples = [
    {"name": "Ravindhra raju", "age": 30},
    {"name": "Meena mokka", "age": 24},
    {"name": "Metymaan kagnkalimi", "age": 90},
    {"name": "Malu dingan", "age": 26}

]

for people in peoples:
    if people["age"] > 25:
        print(people["name"])
# 5
subject_marks = {}
for i in range(3):
    subject = input(f"Enter subject{i+1} name:")
    marks = int(input(f"Enter marks for {subject}:"))
    subject_marks[subject] = marks
    print("marks dictionary")
    print(subject_marks)
    # Calculate average
    total = sum(subject_marks.values())
    print(total/len(subject_marks))
