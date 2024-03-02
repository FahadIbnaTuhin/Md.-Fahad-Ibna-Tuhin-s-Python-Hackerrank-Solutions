import re

results = re.findall(r"(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])", input())
print(*results if results else [-1], sep="\n")
