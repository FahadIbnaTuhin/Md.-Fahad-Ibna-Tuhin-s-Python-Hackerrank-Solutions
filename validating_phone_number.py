import re

for _ in range(int(input())):
    number = input()

    if len(number) == 10 and re.search('^[789]', number) and number.isdigit():
        print('YES')
    else:
        print('NO')