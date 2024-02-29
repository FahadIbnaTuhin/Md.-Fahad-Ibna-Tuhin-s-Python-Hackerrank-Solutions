n1 = int(input())
n1value = set(map(int, input().split()))

n2 = int(input())
n2value = set(map(int, input().split()))

print(len(n1value.symmetric_difference(n2value)))
