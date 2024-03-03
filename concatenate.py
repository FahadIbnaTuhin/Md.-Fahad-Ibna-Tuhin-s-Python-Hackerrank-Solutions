import numpy


def get_array(z):
    array = []

    for _ in range(z):
        row = list(map(int, input().split()))
        array.append(row)

    return array


n, m, p = map(int, input().split())
n_arr, m_arr = get_array(n), get_array(m)
# print(f'{n_arr}\n{m_arr}')

n_array, m_array = numpy.array(n_arr), numpy.array(m_arr)
# print(f'{n_array}\n{m_array}')

print(numpy.concatenate((n_array, m_array)))


# LESSON
# concatenate will give one dimension array
# array_1 = numpy.array([1, 2, 3])
# array_2 = numpy.array([4, 5, 6])
# array_3 = numpy.array([7, 8, 9])
# print(numpy.concatenate((array_1, array_2, array_3)))

# If an array has more than one dimension, it is possible to specify the axis along which multiple arrays are
# concatenated. By default, it is along the first dimension.
# array_1 = numpy.array([[1, 2, 3], [0, 0, 0]])
# array_2 = numpy.array([[0, 0, 0], [7, 8, 9]])
# print(numpy.concatenate((array_1, array_2), axis=1))

