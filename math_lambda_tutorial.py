# Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function
# that has only one line in its body. It proves very handy in functional and GUI programming.
sum = lambda a, b, c: a + b + c
print(sum(1, 2, 3))

power = lambda x: pow(2, 5)
print(power(5))

# The map() function applies a function to every member of an iterable and returns the result. It takes two parameters:
# first, the function that is to be applied and secondly, the iterables.
# Let's say you are given a list of names, and you have to print a list that contains the length of each name.
# print(list(map(len, ['Fahad', 'Sima', 'Kolpona'])))

# print(list(map(str.upper, ['Fahad', 'Bangladesh'])))

# numbers = [2, 5, 6]
# squared_values = list(map(lambda x: x ** 2, numbers))
# print(squared_values)

# from math import factorial
# factorials = list(map(factorial, [3, 5, 6]))
# print(factorials)

# is_even = list(map(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
# print(is_even)

first_characters = list(map(lambda x: x[0], ['apple', 'banana', 'cherry']))
print(first_characters)
