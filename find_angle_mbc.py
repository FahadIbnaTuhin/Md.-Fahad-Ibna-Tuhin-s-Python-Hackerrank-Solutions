import math

AB, BC = int(input()), int(input())

print(round(math.degrees(math.atan(AB / BC))), chr(176), sep='')
