def print_rangoli(size):
    import string

    L = []
    for i in range(size):
        s = string.ascii_letters[i:size]
        # print(s)
        L.append(("-".join(s[::-1] + s[1:])).center(4 * size - 3, "-"))
    # print(L)
    print("\n".join(L[::-1] + L[1:]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
