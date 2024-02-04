def average(array):
    distict_arr = set(array)
    return sum(distict_arr)/len(distict_arr)

    # print(distict_arr)
    # print(sum(arr), len(arr))
    # print(sum(distict_arr), len(distict_arr))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
