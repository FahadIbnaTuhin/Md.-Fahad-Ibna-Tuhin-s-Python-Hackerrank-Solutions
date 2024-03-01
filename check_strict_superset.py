# A strict superset has at least one element that does not exist in its subset.
A = set(map(int, input().split()))
# A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 23, 45, 84, 78}

strict_superset = True
for _ in range(int(input())):
    values = set(map(int, input().split()))

    if not A.issuperset(values):
        strict_superset = False
        break

print(bool(strict_superset))
