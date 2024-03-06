#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    # print(arr)

    # Use the sorted function with a lambda function to sort based on the k-th attribute
    sorted_arr = sorted(arr, key=lambda x: x[k])
    # print(sorted_arr)

    for i in sorted_arr:
        print(*i)

    # This is mine but it is slower
    # seleted_values = [i[k] for i in arr]
    # # print(seleted_values)
    # sorted_value = sorted(seleted_values)
    # # print(sorted_value)
    # final_index = [seleted_values.index(i) for i in sorted_value]
    # # print(final_index)
    # for i in final_index:
    #     print(*arr[i])

