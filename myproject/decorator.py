def log_function(func):
    def wrapper():
        print(f"Running function{func.__name__}")
        func()

    return wrapper


@log_function
def say_goodbye():
    print("Goodbye!")


@log_function
def say_hello():
    print("Hello!")


say_goodbye()
say_hello()
