def count_substring(word, sub_word):
    c = 0
    while word.find(sub_word) != -1:
        c += 1
        word = word[(word.find(sub_word) + 1):]
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
