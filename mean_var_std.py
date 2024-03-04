import numpy

n, _ = map(int, input().split())

arr = numpy.array([input().split() for _ in range(n)], dtype=int)

print(numpy.mean(arr, axis=1), numpy.var(arr, axis=0), round(numpy.std(arr), 11), sep='\n')

# LESSON
# my_array = numpy.array([[1, 2], [3, 4]])

# print(numpy.mean(my_array, axis=0))
# print(numpy.mean(my_array, axis=1))
# print(numpy.mean(my_array, axis=None))
# print(numpy.mean(my_array))

# The var tool computes the arithmetic variance along the specified axis.
# print(numpy.var(my_array, axis=0))
# print(numpy.var(my_array, axis=1))
# print(numpy.var(my_array, axis=None))
# print(numpy.var(my_array))


# print(numpy.std(my_array, axis=0))
# print(numpy.std(my_array, axis=1))
# print(numpy.std(my_array, axis=None))
# print(numpy.std(my_array))

