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
