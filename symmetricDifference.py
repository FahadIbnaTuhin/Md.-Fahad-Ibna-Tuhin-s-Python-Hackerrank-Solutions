M = int(input())
arrM = set(map(int, input().split()))

N = int(input())
arrN = set(map(int, input().split()))

# print(arrM)
# print(arrN)

diff = set()

for i in sorted(arrM.difference(arrN)):
    diff.add(i)
for i in sorted(arrN.difference(arrM)):
    diff.add(i)

for i in sorted(diff):
    print(i)

# 4
# 2 4 5 9
# 4
# 2 4 11 12