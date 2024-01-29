n, m = map(int, input().split())
# n, m = 7, 21
# n, m = 11, 33

c = "-"
d = ".|."

if 5 < n < 101 and 15 < m < 303 and n * 3 == m:
    for i in range(n // 2):
        j = (2 * i) + 1
        print((d*j).center(m, c))

    print("WELCOME".center(m, c))

    for i in range((n // 2) - 1, -1, -1):
        j = (2 * i) + 1
        print((d * j).center(m, c))
