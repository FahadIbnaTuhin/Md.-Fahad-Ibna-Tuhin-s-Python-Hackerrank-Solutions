import re


def wrapper(f):
    def fun(l):
        # print(l)
        return f([f"+91 {el[len(el) - 10:][:5]} {el[len(el) - 10:][5:]}" for el in l])
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
