class UnderAgeError(Exception):
    """Raised when the input is under age"""
    pass


x = int(input("Enter your Age:"))
try:
    if not x.isdigit():
        raise TypeError("Age must be a number.")

    age = int(x)
    if x < 18:
        raise UnderAgeError("UnderAgeError")

    else:
        print("Access granted")
except UnderAgeError as e:
    print("You must be at least 18 years old.:", e)
except TypeError as t:
    print("Type Error", t)
