import numpy


n, _ = map(int, input().split())
arr = []

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

# print(arr)
num_arr = numpy.array(arr, dtype=int)
# print(arr)
numpy.set_printoptions(legacy='1.13')
print(numpy.var(num_arr, axis=0))

# print([i for i in numpy.mean(num_arr, axis=1)])
# print(numpy.var(num_arr, axis=0, dtype=float))
# print(numpy.std(num_arr))

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

