import numpy
# In order to get alignment correct, please insert the line below the numpy import
numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
print(numpy.eye(n, m))


# LESSON
# The identity tool returns an identity array. An identity array is a square matrix with all the main diagonal
# elements as 1 and the rest as 0. The default type of elements is float.
# Identity Metrix called in Bengali is Ekok/Ovedok Matrix
# print(numpy.identity(3))

# eye:  is for the upper diagonal, a negative k is for the lower, and a 0 k (default) is for the main diagonal.
# print(numpy.eye(2, 5))
# print(numpy.eye(5, 5, 2))
# print(numpy.eye(5, 5, -2))
