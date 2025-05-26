students = {
    "Arjun": 85,
    "Bhavna": 42,
    "Chetan": 74,
    "Divya": 58,
    "Eshan": 91,
    "Farah": 37
}
results = {}
total_pass = 0
total_fail = 0
for name, marks in students.items():
    if marks >= 50:
        result = "pass"
    else:
        result = "fail"
    print(f"{name}:{result}")

    if result in 'pass':
        total_pass += 1
    else:
        total_fail += 1
print(f"{total_pass} and {total_fail}")

with open("fileoperation.txt", "w") as file:
    file.write("File operation-write")
