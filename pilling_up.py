# https://www.youtube.com/watch?v=vql_CGVnTc0

for _ in range(int(input())):
    _ = int(input())
    a = list(map(int, input().split()))
    arr = []
    arrl = len(a)

    i = 0
    while arrl > 0:
        # print(a[i], a[- 1 - i])
        if arrl == 1:
            arr.append(a[0])
            break
        elif a[i] < a[- 1 - i]:
            arr.append(a.pop())
        elif a[i] > a[- 1 - i]:
            arr.append(a.pop(0))
        else:
            arr.append(a.pop())

    print('Yes') if arr == sorted(arr, reverse=True) else print('No')


# LESSON
# a = [1, 2, 3, 7, 8]
# b = [8, 7, 3, 2, 1]
# c = [4, 3, 2, 1, 3, 4]
# d = [1, 3, 2]
#
# arr = []
# i = 0
# while len(c) >= 0:
#     print(c[i], c[- 1 - i])
#     if len(c) == 1:
#         arr.append(c[0])
#         break
#     elif c[i] < c[- 1 - i]:
#         arr.append(c[- 1 - i])
#         c.pop()
#     elif c[i] > c[- 1 - i]:
#         arr.append(c[i])
#         c.pop(0)  # To pop the first element
#     else:
#         arr.append(c[- 1 - i])
#         c.pop()
#
# print(arr)
# # a = [8, 9, 7, 6, 5, 5, 1]
# print('Yes') if arr == sorted(arr, reverse=True) else print('No')
