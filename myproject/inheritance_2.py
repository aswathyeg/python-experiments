class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        # Use super() to call Employee's constructor
        super().__init__(name, salary)

        # Assign department to self.department
        self.department = department


# Create a Manager object and print name, salary, and department
m = Manager("Alice", 3000000, "IT")
print(f"{m.name},{m.salary},{m.department}")
