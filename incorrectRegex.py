import re

n = int(input())

for _ in range(n):
    try:
        print(bool(re.compile(input())))
    except:
        print('False')
