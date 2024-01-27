# any() and all() return bool (true or false).

# 1st Method
# def isAlphanumeric(st):
#     return any(i.isalnum() for i in st)
# def isAlphabetical(st):
#     return any(i.isalpha() for i in st)
# def isDigit(st):
#     return any(i.isdigit() for i in st)
# def isLowercase(st):
#     return any(i.islower() for i in st)
# def isUppercase(st):
#     return any(i.islower() for i in st)
# if __name__ == '__main__':
#     s = input()
#     print(isAlphanumeric(s))
#     print(isAlphabetical(s))
#     print(isDigit(s))
#     print(isLowercase(s))
#     print(isUppercase(s))

# 2nd Method
def check_condition(st):
    conditions = {
        'isAlphanumeric': any(i.isalnum() for i in st),
        'isAlphabetical': any(i.isalpha() for i in st),
        'isDigit': any(i.isdigit() for i in st),
        'isLowercase': any(i.islower() for i in st),
        'isUppercase': any(i.isupper() for i in st)
    }

    for key, value in conditions.items():
        print(value)


if __name__ == '__main__':
    s = input()
    check_condition(s)
