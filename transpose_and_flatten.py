import numpy

n, m = map(int, input().split())

array = []
for _ in range(n):
    values = list(map(int, input().split()))
    array.append(values)

# print(array)
my_array = numpy.array(array)
print(my_array.transpose())
print(my_array.flatten())

# LESSON
# my_array = numpy.array([[1, 2, 3], [4, 5, 6]])
# print(my_array)

# transpose: We can generate the transposition of an array using the tool
# print(numpy.transpose(my_array))

# flatten: The tool flatten creates a copy of the input array flattened to one dimension.
# print(my_array.flatten())


