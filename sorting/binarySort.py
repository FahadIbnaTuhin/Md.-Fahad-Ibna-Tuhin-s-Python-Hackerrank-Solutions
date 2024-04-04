def binarySort(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


result = binarySort([1, 2, 3, 4, 5, 6, 7], 5)
print(result)

# https://www.youtube.com/watch?v=6ysjqCUv3K4&list=PLBZBJbE_rGRV8D7XZ08LK6z-4zPoWzu5H&index=10