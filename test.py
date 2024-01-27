def isAlphabetical(st):
    return any(i.isalpha() for i in st)
    # return "True" for i in st if i.isalpha() else "False"


if __name__ == '__main__':
    s = input()
    print(isAlphabetical(s))
