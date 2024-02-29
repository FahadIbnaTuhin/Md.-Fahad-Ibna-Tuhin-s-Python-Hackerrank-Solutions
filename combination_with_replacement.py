# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)

if s.isupper() and 0 < k <= len(s):
    for i in combinations_with_replacement(sorted(s), k):
        print(*i, sep='')
