from collections import namedtuple

N = int(input())

if 0 < N <= 100:
    n1, n2, n3, n4 = map(str, input().split())
    Database = namedtuple("Database", "ID MARKS CLASS NAME")
    for i in range(N):
        v1, v2, v3, v4 = input().split()
        if n1 in Database._fields:
            print(v3)
