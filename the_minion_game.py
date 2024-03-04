def minion_game(string):
    s = len(string)
    vowel, consonant = 0, 0

    for i in range(s):
        if string[i] in "AEIOU":
            vowel += (s - i)
        else:
            consonant += (s - i)

    if vowel < consonant:
        print(f'Stuart {consonant}')
    elif vowel > consonant:
        print(f'Kevin {vowel}')
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)


# My Wrong Code:
# def generate_substring(s):
#     arrays = set()
#     for i in range(len(s)):
#         for j in range(i + 1, len(s) + 1):
#             arrays.add(s[i:j])
#     return arrays
#
#
# def minion_game(string):
#     stuarts_score, kelvin_score = 0, 0
#
#     sub_strings = list(generate_substring(string))
#     # print(sub_strings)
#
#     for i in sub_strings:
#         if i[0].upper() in "AEIOU":
#             kelvin_score += string.count(i)
#         else:
#             stuarts_score += string.count(i)
#     # print(stuarts_score, kelvin_score)
#
#     if stuarts_score > kelvin_score:
#         print(f'Stuart {stuarts_score}')
#     elif stuarts_score < kelvin_score:
#         print(f'Kevin {kelvin_score}')
#     else:
#         print('Draw')
#
#
# if __name__ == '__main__':
#     s = input()
#     minion_game(s)
