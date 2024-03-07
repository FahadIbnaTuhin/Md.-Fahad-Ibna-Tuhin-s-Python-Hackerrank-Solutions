from collections import Counter

# Using sorted, so that when two values are same, It show them alphabetically
inp = sorted(input().strip())

# Using most_common(3) to get the first 3
s = Counter(inp).most_common(3)
print(s)

for i in s:
    print(*i)
