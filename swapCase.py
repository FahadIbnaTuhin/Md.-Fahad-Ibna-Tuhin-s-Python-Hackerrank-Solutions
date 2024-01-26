def swap_case(inp):
    out = ""
    for letter in inp:
        if letter.isalpha():
            if letter.isupper():
                out += letter.lower()
            else:
                out += letter.upper()
        else:
            out += letter
    return out


if __name__ == '__main__':
    s = input()
    swap_case(s)
    result = swap_case(s)
    print(result)
