# https://www.youtube.com/watch?v=vql_CGVnTc0
# 2
# 6
# 4 3 2 1 3 4
# 3
# 1 3 2
for _ in range(int(input())):
    input()
    arr = [int(i) for i in input().split()]
    minimum_value_index = arr.index(min(arr))
    left = arr[:minimum_value_index]
    right = arr[minimum_value_index + 1:]
    if left == sorted(left, reverse=True) and right == sorted(right):
        print('Yes')
    else:
        print('No')
