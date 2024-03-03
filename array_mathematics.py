import numpy as np

n, _ = map(int, input().split())

a, b = [np.array([list(map(int, input().split())) for _ in range(n)]) for _ in range(2)]

print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')


# LESSON
# a = numpy.array([1, 2, 3, 4], float)
# b = numpy.array([5, 6, 7, 8], float)

# print(f'{a + b} = {numpy.add(a, b)}')
# print(f'{a - b} = {numpy.subtract(a, b)}')
# print(f'{a * b} = {numpy.multiply(a, b)}')
# print(f'{a / b} = {numpy.divide(a, b)}')
# There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.
# print(f'{a / b} = {numpy.floor_divide(a, b)}')
# print(f'{a / b} = {numpy.floor_divide(a, b).astype(int)}')
# print(f'{a % b} = {numpy.mod(a, b)}')
# print(f'{a ** b} = {numpy.power(a, b)}')
