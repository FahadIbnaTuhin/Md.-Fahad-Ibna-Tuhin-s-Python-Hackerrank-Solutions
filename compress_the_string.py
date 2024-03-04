s = input()
result = []

i = 0
while i < len(s):
    count = 1
    j = i + 1
    while j < len(s) and s[i] == s[j]:
        count += 1
        j += 1
    result.append((count, int(s[i])))
    i = j

print(*result, sep=' ')
