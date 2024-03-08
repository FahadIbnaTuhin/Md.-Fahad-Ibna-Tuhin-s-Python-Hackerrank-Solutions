from itertools import product

k, m = map(int, input().split())
arr = []

for _ in range(k):
    _, *elements = map(int, input().split())
    arr.append(elements)

# print(arr)
combinations = list(product(*arr))
# print(combinations)

result = max(sum(i ** 2 for i in combination) % m for combination in combinations)
print(result)
