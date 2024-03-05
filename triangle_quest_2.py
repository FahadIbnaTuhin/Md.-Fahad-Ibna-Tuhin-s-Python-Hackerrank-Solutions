# We have to use just one print and for statement. So, we will use this formula shown on this youtube channel
# https://www.youtube.com/watch?v=kHcv1tGnF5Y
# Remember this 10^3/9 = 111, 10^4/9=1111 and so on
for n in range(1, int(input()) + 1):
    print(((10 ** n) // 9) ** 2)

# LESSON
# end is used to specify what should be printed at the end of the line
# print("Hello", end=' ')
# print("World")          # Hello World
# sep is used to specify the separator between the items that are passed to the print function.# Okay but this will not
# be accepted as the last line using string concat and also using str
# print("One", "Two", "Three", sep='-')   # One-Two-Three


# for i in range(int(input())):
#     first = ''.join(str(j) for j in range(1, i + 2))
#     print(first + first[:-1][::-1])

# for n in range(int(input())):
#     palin = list(range(1, n + 2)) + list(range(n, 0, -1))
#     print(*palin, sep='')
