def partition(arr, l, r):
    """
    Taken an array with left index and right index and then return the pivot element index, whose left
    side all the elements that are less then the pivot, on the right side elements with higher value than pivot.
    Pivot's left and right side doesn't need to be in order
    :param arr: array
    :param l: left index
    :param r: right index
    :return: pivot index
    """
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):  # not including r
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1
# result = partition([-2, 3, -1, 5, 4, -3, 0], 0, 6)
# print(result)


def quick_sort(arr, l, r):
    """
    Sorts the array using the QuickSort algorithm.
    :param arr: array to be sorted
    :param l: left index
    :param r: right index
    """
    if l >= r:
        return
    p = partition(arr, l, r)
    quick_sort(arr, l, p - 1)
    quick_sort(arr, p + 1, r)


arr = [-2, 3, -1, 5, 4, -3, 0]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

# https://www.youtube.com/watch?v=0SkOjNaO1XY&list=PLBZBJbE_rGRV8D7XZ08LK6z-4zPoWzu5H&index=11
