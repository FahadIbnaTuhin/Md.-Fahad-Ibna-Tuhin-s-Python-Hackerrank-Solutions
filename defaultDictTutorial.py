from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(n):
    d['A'].append(input())
for i in range(m):
    d['B'].append(input())
# print(d)

for i in range(len(d['B'])):
    count = 0
    for j in range(len(d['A'])):
        if d['B'][i] == d['A'][j]:
            print(j + 1, end=" ")
            count += 1
        if j == len(d['A']) - 1 and count == 0:
            print("-1", end="")
    print()


# 5 2
# a
# a
# b
# a
# b
# a
# b
