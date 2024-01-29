# n = int(input())
n = 17





for i in range(1, n + 1):
    if "0" in str(i):
        gap = 5 - len(str(i))
        total = (" " * gap) + str(i)
        print(f"{total}")
        continue
    print(f"{str(i).zfill(5).replace("0", " ")}")

#     {oct(i)[2:]}    {hex(i)[2:]}    {bin(i)[2:]}