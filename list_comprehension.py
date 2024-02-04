def solve(x, y, z, n):
    output = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
    return output
    # for i in range(x + 1):
    #     for j in range(y + 1):
    #         for k in range(z + 1):
    #             if (i + j + k) != n:
    #                 output.append([i, j, k])


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # x, y, z, n = 1, 1, 2, 3
    result = solve(x, y, z, n)
    print(result)
