# set comprehension
numbers = [1, 2, 3, 4, 5, 6, 7]
odd_square = {x**2 for x in numbers if x % 2 != 0}
print(odd_square)

# dictionary comprehension
words = ["apple", "banana", "kiwi"]
dictionary = {word: len(word) for word in words}
print(dictionary)
