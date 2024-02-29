def calculate(num1, op, num2):
    operation = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        'x': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    if op in operation:
        return operation[op](num1, num2)
    else:
        raise ValueError('Invalid operation')


a, b, c = input().split()
a, c = map(float, (a, c))

print(calculate(a, b, c))
