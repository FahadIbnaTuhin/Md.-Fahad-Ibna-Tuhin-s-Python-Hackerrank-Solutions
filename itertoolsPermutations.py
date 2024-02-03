from itertools import permutations

s, k = map(str, input().split())
# s, k = "HACK", "2"

if 0 < int(k) <= len(s):
    for i in permutations(sorted(s), int(k)):
        print(f"{i[0]}{i[1]}")
