# If "K is a factor of n," it means that K is a whole number (integer) that divides evenly into n, leaving no remainder.
# K=3, n=12 so n/k=4 no remainder, so k is a factor of n


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i: i + k]
        lst = list()
        for char in substring:
            if char not in lst:
                lst.append(char)
        print(*lst, sep='')


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
