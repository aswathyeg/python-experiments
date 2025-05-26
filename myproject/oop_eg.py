class Student:
    # note:2 underscores needed
    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber

    def display_info(self):
        print(f"Name:{self.name} and Roll number:{self.rollnumber}")


p1 = Student("Alice", 19)
p1.display_info()
