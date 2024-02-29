n1 = int(input())
n1values = set(map(int, input().split()))

n2 = int(input())
n2values = set(map(int, input().split()))

result = n1values.intersection(n2values)
print(len(result))
