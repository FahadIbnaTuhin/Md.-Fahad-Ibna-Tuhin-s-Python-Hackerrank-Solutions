import sys

n = int(input())
A = set(map(int, input().split()))
# A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24, 52}

for _ in range(int(input())):
    m, n = input().split()
    values = set(map(int, input().split()))
    if m == 'intersection_update':
        A.intersection_update(values)
    elif m == 'symmetric_difference_update':
        A.symmetric_difference_update(values)
    elif m == 'difference_update':
        A.difference_update(values)
    elif m == 'update':
        A.update(values)
    else:
        print('Wrong Input')
        sys.exit(1)

print(sum(A))
# print(A)
