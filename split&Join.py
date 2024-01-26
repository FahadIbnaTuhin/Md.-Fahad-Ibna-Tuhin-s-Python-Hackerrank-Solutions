def split_and_join(line):
    line_list = line.split(" ")
    line_txt = "-".join(line_list)
    return line_txt


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
