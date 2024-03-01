from collections import Counter

k = int(input())
values = list(map(int, input().split()))

value_counts = Counter(values)

for i in set(values):
    if k != value_counts[i]:
        print(i)
        break
