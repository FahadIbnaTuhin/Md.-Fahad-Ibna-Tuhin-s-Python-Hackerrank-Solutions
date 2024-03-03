import numpy

values = list(map(int, input().split()))

if len(values) == 9:
    array = numpy.array(values)
    print(numpy.reshape(array, (3, 3)))


# LESSON
# my__1D_array = numpy.array([1, 2, 3, 4, 5])
# print(my__1D_array.shape)
# (5,) -> 1 row and 5 columns

# my__2D_array = numpy.array([[1, 2], [3, 4], [6, 5]])
# print(my__2D_array.shape)
# (3, 2) -> 3 rows and 2 columns

# Using Shape to change array dimensions
# change_array = numpy.array([1, 2, 3, 4, 5, 6])
# change_array.shape = (3, 2)
# print(change_array)

# The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify
# the original array itself.

# my_array = numpy.array([1, 2, 3, 4, 5, 6])
# print(numpy.reshape(my_array, (3, 2)))


