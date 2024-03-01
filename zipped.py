n, x = map(int, input().split())

values = []
for i in range(x):
    value = map(float, input().split())
    values.append(value)

for i in zip(*values):
    print(sum(i) / x)
