def solve(s):
    word_list = s.split(" ")
    new_sen = ""
    for word in word_list:
        new_sen += word.capitalize() + " "
    return new_sen


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
