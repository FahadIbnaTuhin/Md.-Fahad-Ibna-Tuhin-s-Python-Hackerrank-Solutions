from datetime import datetime
import math
import os
import random
import re
import sys


def time_delta(t1, t2):  # Day dd Mon yyyy hh:mm:ss +xxxx
    time_format = "%a %d %b %Y %H:%M:%S %z"

    date1 = datetime.strptime(t1, time_format)
    date2 = datetime.strptime(t2, time_format)

    time_difference = int(abs((date1 - date2).total_seconds()))
    return time_difference


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)
