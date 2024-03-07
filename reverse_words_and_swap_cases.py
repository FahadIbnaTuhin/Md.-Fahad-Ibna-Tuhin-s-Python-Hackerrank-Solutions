import os


def reverse_words_order_and_swap_cases(sentence):
    sentence_list = sentence.split()[::-1]
    output = ''
    for word in sentence_list:
        for letter in word:
            output += letter.upper() if letter.islower() else letter.lower()
        output += ' '
    return output.rstrip()


if __name__ == '__main__':
    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    print(result)
