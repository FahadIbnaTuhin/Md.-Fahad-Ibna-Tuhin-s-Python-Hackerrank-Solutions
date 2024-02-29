n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    values = input().split()
    if values[0] == 'pop':
        try:
            s.pop()
        except KeyError:
            pass  # Ignore KeyError if set is empty
    elif values[0] == 'remove':
        s.remove(int(values[1]))
    elif values[0] == 'discard':
        s.discard(int(values[1]))

print(sum(s))
