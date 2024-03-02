def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1

    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence


print(generate_fibonacci(int(input())))
