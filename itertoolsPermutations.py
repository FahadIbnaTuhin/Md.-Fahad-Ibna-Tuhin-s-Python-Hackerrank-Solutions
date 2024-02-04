from itertools import permutations

S, k = input().split()

a = "\n".join(sorted("".join(p) for p in permutations(S, int(k))))

print(a)