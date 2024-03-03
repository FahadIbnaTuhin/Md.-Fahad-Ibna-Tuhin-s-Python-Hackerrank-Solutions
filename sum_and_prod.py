import numpy

n, _ = map(int, input().split())

arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    # print(row)
    arr.append(row)

# print(arr)
arr = numpy.array(arr)
arr_sum = numpy.sum(arr, axis=0)
print(numpy.prod(arr_sum))

# LESSON
# my_array = numpy.array([[1, 2], [3, 4]])
# print(numpy.sum(my_array, axis=0))  # vertical
# print(numpy.sum(my_array, axis=1))  # Horizental
# print(numpy.sum(my_array, axis=None))
# print(numpy.sum(my_array))

# print(numpy.prod(my_array, axis=0))
# print(numpy.prod(my_array, axis=1))
# print(numpy.prod(my_array, axis=None))
# print(numpy.prod(my_array))
