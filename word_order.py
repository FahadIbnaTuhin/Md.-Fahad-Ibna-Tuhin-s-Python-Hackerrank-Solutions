values = [input() for _ in range(int(input()))]

print(len(set(values)))

number_of_values = {}
for i in values:
    if i in number_of_values:
        number_of_values[i] += 1
    else:
        number_of_values[i] = 1

print(*number_of_values.values())
