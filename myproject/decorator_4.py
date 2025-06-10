def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function with arguments:{','.join(map(str, args))}")
        return func(*args, **kwargs)
    return wrapper


@log_args
def add(a, b):
    return a + b


print(add(3, 4))
