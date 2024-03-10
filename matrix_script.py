import re

n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(input())
# print(matrix)

decoded_script = ''
for i in zip(*matrix):
    for j in i:
        decoded_script += j

# print(decoded_script)
cleaned_string = re.sub(r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])", " ", decoded_script)
print(cleaned_string.strip())


#  Let's break down the regular expression (?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9]) step by step:
#
# (?<=[a-zA-Z0-9]): This is a positive lookbehind assertion. It checks if there is an alphanumeric character (a letter
# or digit) immediately preceding the current position in the string.
#
# [^a-zA-Z0-9]+: This part matches one or more consecutive characters that are not alphanumeric. The ^ inside the square
# brackets negates the character class, meaning it matches anything that is not in the set of uppercase letters (A-Z),
# lowercase letters (a-z), or digits (0-9).
#
# (?=[a-zA-Z0-9]): This is a positive lookahead assertion. It checks if there is an alphanumeric character immediately
# following the current position in the string.
#
# Putting it all together, the regular expression as a whole:
#
# Looks for sequences of characters that are not alphanumeric ([^a-zA-Z0-9]+).
# Ensures that these sequences are surrounded by alphanumeric characters on both sides ((?<=[a-zA-Z0-9]) and
# (?=[a-zA-Z0-9])).
