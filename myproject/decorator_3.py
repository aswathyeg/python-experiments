# Your decorator here
def shout_decorator(func):
    def wrapper():
        print("!!!")
        func()
        print("!!!")
    return wrapper


@shout_decorator
def greet():
    print("Welcome!")


greet()
