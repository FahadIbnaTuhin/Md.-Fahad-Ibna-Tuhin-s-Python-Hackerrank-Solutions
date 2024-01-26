if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = [item for item in integer_list]
    t = tuple(t)
    print(hash(t))
