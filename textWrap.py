import textwrap


def wrap(string, max_width):
    li = [f"{item}\n" for item in textwrap.wrap(string, max_width)]
    return "".join(li)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
