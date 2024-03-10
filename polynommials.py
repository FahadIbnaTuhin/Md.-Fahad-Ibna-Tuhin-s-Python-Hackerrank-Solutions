import numpy

p = list(map(float, input().split()))
v = int(input())

print(numpy.polyval(p, v))
