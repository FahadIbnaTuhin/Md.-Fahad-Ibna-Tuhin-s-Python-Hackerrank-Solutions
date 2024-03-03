import numpy

dimension = tuple(map(int, input().split()))
# print(dimension)

print(f'{numpy.zeros(dimension, dtype=int)}\n{numpy.ones(dimension, dtype=int)}')


# LESSON
# Zeros: returns a new array with a given shape and type filled with 0's.
# print(numpy.zeros((1, 2)))
# print(numpy.zeros((1, 2), dtype=int))

# ones: The ones tool returns a new array with a given shape and type filled with 1's.
# print(numpy.ones((2, 3)))
# print(numpy.ones((2, 3), dtype=int))
