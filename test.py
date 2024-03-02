import re

uid = input()

if re.findall(r'[A-Z]{2,}[0-9]{3,}', uid) and len(uid) == 10 and set(uid) == len(uid):
    print('Valid')
else:
    print('Invalid')


