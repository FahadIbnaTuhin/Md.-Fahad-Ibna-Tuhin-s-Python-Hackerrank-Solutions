s = input().strip()
lower = [i for i in s if i.islower()]
upper = [i for i in s if i.isupper()]
digits = [i for i in s if i.isdigit()]
# print(f'{sorted(lower)}\n{sorted(upper)}')

odd, even = [i for i in digits if int(i) % 2 != 0], [i for i in digits if int(i) % 2 == 0]
# print(f'{odd}\n{even}')

print(''.join(sorted(lower) + sorted(upper) + sorted(odd) + sorted(even)))
