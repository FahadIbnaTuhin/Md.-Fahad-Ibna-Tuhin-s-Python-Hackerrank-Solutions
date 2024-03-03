import numpy

n, _ = map(int, input().split())
arr = []

for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

# print(arr)
num_arr = numpy.array(arr)
min_num_arr = numpy.min(num_arr, axis=1)
# print(min_num_arr)
print(numpy.max(min_num_arr))



# LESSON
# my_array = numpy.array([[2, 5],
#                         [3, 7],
#                         [1, 3],
#                         [4, 0]])

# print(numpy.min(my_array, axis=0))
# print(numpy.min(my_array, axis=1))
# print(numpy.min(my_array, axis=None))
# print(numpy.min(my_array))

# print(numpy.max(my_array, axis=0))
# print(numpy.max(my_array, axis=1))
# print(numpy.max(my_array, axis=None))
# print(numpy.max(my_array))
