# https://www.youtube.com/watch?v=kk1d1ehu0vg

from itertools import combinations

input()
l = [i for i in input().split()]
k = int(input())
c = list(combinations(l, k))
r = [i for i in c if 'a' in i]
# print(c, r, sep='\n')

print('%0.3f' % (len(r) / len(c)))
