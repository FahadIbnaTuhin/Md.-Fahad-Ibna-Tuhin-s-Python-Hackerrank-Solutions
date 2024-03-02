for _ in range(int(input())):
    inp = input().strip()

    try:
        float_value = float(inp)
    except ValueError:
        is_float = False
    else:
        is_float = True if '.' in inp else False

    print(str(is_float))

# for _ in range(int(input())):
#     inp = input().strip()
#
#     is_float = True
#     try:
#         float(inp)
#     except ValueError:
#         is_float = False
#     else:
#         if not inp.startswith(('+', '-', '.')) and inp.startswith(('+-', '-+')):
#             is_float = False
#         elif inp[inp.index('.') + 1] == '':
#             is_float = False
#         elif inp.count('.') != 1:
#             is_float = False
#
#     print(str(is_float))
