import numpy


def arrays(array):
    a = numpy.array(array, float)
    return a[::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)


# Lesson
# import numpy
#
# a = numpy.array([1, 2, 3, 4, 5])
# print(a[1])
#
# b = numpy.array([1, 2, 3, 4, 5], float)
# print(b[1])
