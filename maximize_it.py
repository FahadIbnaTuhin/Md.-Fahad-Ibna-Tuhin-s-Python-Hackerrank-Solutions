k, m = map(int, input().split())

sum = 0
for _ in range(k):
    row = list(map(int, input().split()))
    sum += max(row) ** 2

print(sum % m)


