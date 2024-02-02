def result(space, num, not_last=True):
    if not_last:
        if "0" in num:
            gap = space - len(num)
            total = (" " * gap) + num
            print(f"{total}", end="")
        else:
            print(f"{num.zfill(space).replace('0', ' ').upper()}", end="")
    else:
        if "0" in num:
            gap = space - len(num)
            total = (" " * gap) + num
            print(f"{total}")
        else:
            print(f"{num.zfill(space).replace('0', ' ').upper()}")


def print_formatted(n):
    gap = len(bin(n)[2:]) + 1
    # print(gap)
    for i in range(1, n + 1):
        number = str(i)
        result(gap - 1, number)

        # Octal
        number = str(oct(i)[2:])
        result(gap, number)

        # Hex
        number = str(hex(i)[2:])
        result(gap, number)

        # Bin
        number = str(bin(i)[2:])
        result(gap, number, not_last=False)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
