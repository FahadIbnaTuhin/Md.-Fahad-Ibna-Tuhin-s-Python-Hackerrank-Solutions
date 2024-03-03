import numpy
numpy.set_printoptions(legacy='1.13')

values = numpy.array(list(map(float, input().split())))

print(f'{numpy.floor(values)}\n{numpy.ceil(values)}\n{numpy.rint(values)}')

# LESSON
# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# print(numpy.floor(my_array))
# print(numpy.ceil(my_array))
# print(numpy.rint(my_array))
