import re

for _ in range(int(input())):
    # The positive lookbehind (?<=.) ensures that there's at least one character preceding the '#'.
    result = re.findall(r"(?<=.)#[a-fA-F0-9]{3,6}", input())
    if result:
        print(*result, sep="\n")
