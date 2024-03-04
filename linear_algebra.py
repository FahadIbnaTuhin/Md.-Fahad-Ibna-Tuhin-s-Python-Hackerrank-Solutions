import numpy

n = int(input())
values = [list(map(float, input().split())) for _ in range(n)]
# print(values)
matrix = numpy.array(values)
print(round(numpy.linalg.det(matrix), 2))

# LESSON
# matrix = numpy.array([[1, 2], [2, 1]])
# The linalg.det tool computes the determinant of an array.
# print(numpy.linalg.det(matrix))

# The linalg.eig computes the eigenvalues and right eigenvectors of a square array.
# print(numpy.linalg.eig(matrix))
# vals, vecs = numpy.linalg.eig(matrix)
# print(vals)
# print(vecs)

# The linalg.inv tool computes the (multiplicative) inverse of a matrix.
# print(numpy.linalg.inv(matrix))
