# pow(a, b, m) means: (a ** b) % m
# Note: Here, a and b can be floats or negatives, but, if a third argument is present, b cannot be negative.

a, b, c = int(input()), int(input()), int(input())

print(f'{a**b}\n{pow(a, b, c)}')
