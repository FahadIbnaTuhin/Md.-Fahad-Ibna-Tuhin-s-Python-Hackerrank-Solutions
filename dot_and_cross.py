import numpy

n = int(input())

A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(n)]
# print(f'{A}\n{B}')

a_arr, b_arr = numpy.array(A), numpy.array(B)
print(numpy.dot(a_arr, b_arr))



# LESSON
# A = numpy.array([1, 2])
# B = numpy.array([3, 4])
#
# print(numpy.dot(A, B))
# print(numpy.cross(A, B))
