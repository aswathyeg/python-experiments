# A generator is a function that yields values one at a time using yield instead of return.
# Benefits of Generators:
# Memory-efficient: No need to store the whole sequence in memory.

# Lazy evaluation: Values are produced only when needed.

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


counter = count_up_to(3)
print(next(counter))  # ➜ 1
print(next(counter))  # ➜ 2
