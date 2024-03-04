import numpy

A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))

print(f'{numpy.inner(A, B)}\n{numpy.outer(A, B)}')


# LESSON
# A = numpy.array([0, 1])
# B = numpy.array([3, 4])
#
# print(numpy.inner(A, B))
# print(numpy.outer(A, B))
