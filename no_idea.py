# x ∈ A means that element x is a member of set A.
from collections import Counter

n, _ = map(int, input().split())

# for _ in range(n):
elements = list(map(int, input().split()))
A, B = set(map(int, input().split())), set(map(int, input().split()))

element_count = Counter(elements)

pre = sum(element_count[a] for a in A) - sum(element_count[b] for b in B)
# Counter(elements)[a]
print(pre)
