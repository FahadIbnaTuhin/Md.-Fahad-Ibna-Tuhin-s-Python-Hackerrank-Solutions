n = int(input())

for i in range(n):
    n1 = int(input())
    n1values = set(map(int, input().split()))
    n2 = int(input())
    n2values = set(map(int, input().split()))

    print(bool(n1values.issubset(n2values)))
