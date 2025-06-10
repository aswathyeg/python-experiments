def greet_decorator(func):
    def wrapper(name):
        print("Preparing to greet..")
        func(name)
        print("Greeted")
    return wrapper


@greet_decorator
def greet(name):
    print(f"Hello,{name}")


greet("Alice")
