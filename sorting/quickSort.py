def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i + 1]
    arr[i + 1] = arr[r]
    arr[r] = temp
    return i + 1


result = partition([-2, 3, -1, 5, 4, -3, 0], 0, 6)
print(result)
