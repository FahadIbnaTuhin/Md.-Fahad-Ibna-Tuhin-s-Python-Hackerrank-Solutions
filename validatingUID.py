import re

for _ in range(int(input())):
    uid = input()
    if re.match(r'^[A-Z]{2,}[0-9]{3,}$', uid) and len(uid) == 10 and len(set(uid)) == len(uid):
        print('Valid')
    else:
        print('Invalid')

# Replaced re.findall with re.match to ensure that the entire string matches the pattern.