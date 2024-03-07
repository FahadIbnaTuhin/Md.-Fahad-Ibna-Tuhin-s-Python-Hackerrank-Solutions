import os


def avg(*args):
    arr = [i for i in args]
    average = sum(arr) / len(arr)
    return f'{average:.2f}'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = map(int, input().split())
    res = avg(*nums)

    fptr.write('%.2f' % res + '\n')

    fptr.close()
