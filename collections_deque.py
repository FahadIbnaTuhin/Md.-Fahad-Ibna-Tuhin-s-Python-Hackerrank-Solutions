from collections import deque
import sys

d = deque()
n = int(input())

for _ in range(n):
    values = input().split()
    if values[0] == 'append':
        d.append(values[1])
    elif values[0] == 'appendleft':
        d.appendleft(values[1])
    elif values[0] == 'popleft':
        d.popleft()
    elif values[0] == 'pop':
        d.pop()
    else:
        print('Wrong Input')
        sys.exit(1)

print(' '.join(d))
