from functools import reduce
celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit)

# filter
names = ["Ann", "Bob", "Clara", "Dave"]
name_list = list(filter(lambda name: len(name) > 3, names))
print(name_list)

# reduce
nums = [1, 2, 3, 4]
multiply = reduce((lambda x, y: x*y), nums)
print(multiply)

words = ["sun", "planet", "galaxy", "universe", "star"]
longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest)
