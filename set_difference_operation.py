n1 = int(input())
n1values = set(map(int, input().split()))

n2 = int(input())
n2values = set(map(int, input().split()))

print(len(n1values.difference(n2values)))
