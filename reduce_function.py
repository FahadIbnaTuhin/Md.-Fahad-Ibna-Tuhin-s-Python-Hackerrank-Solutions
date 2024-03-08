from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))

    # print(fracs)
    result = product(fracs)
    print(*result)

# LESSON
# The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to
# right to reduce it to one value. Say you have a list, say [1,2,3] and you have to find its sum.
# reduce(lambda x, y : x + y,[1,2,3])  # 6
# You can also define an initial value. If it is specified, the function will assume initial value as the value given,
# and then reduce. It is equivalent to adding the initial value at the beginning of the list. For example:
# reduce(lambda x, y : x + y, [1,2,3], -3)  # 3
# from fractions import gcd
# reduce(gcd, [2,4,8], 3)  # 1

# Rational numbers are numbers that can be expressed as the quotient or fraction of two integers, where the numerator is
# an integer and the denominator is a non-zero integer. In other words, a rational number is any number that can be
# written in the form a/b, where a and  b are integers and b is not equal to 0
# E.g. 1/2, -3/4, 5, 0, 7(7/1)
