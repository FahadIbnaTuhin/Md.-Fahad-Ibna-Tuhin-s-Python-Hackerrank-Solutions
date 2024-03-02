# A palindromic number (also known as a numeral palindrome or a numeric palindrome) is a number (such as 16461) that
# remains the same when its digits are reversed. E.g. : 16461

n1 = int(input())
n1value = input().split()

print('True') if all(int(i) > 0 for i in n1value) and any(i == i[::-1] for i in n1value) else print('False')

# if all(int(x) > 0 for x in n1value) and any(x == x[::-1] for x in n1value):
#     print('True')
# else:
#     print('False')

