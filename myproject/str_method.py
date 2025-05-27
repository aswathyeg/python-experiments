class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # Define a __str__ method to return something like:
    # "Student: Alice, Grade: A"
    def __str__(self):
        return f"Student:{self.name},Grade:{self.grade}"


b = Student("Alice", "A")
print(b)

for idx, val in enumerate(['a', 'b', 'c']):
    print(idx, val)


cube = [i**3 for i in range(1, 10)]
print(cube)
