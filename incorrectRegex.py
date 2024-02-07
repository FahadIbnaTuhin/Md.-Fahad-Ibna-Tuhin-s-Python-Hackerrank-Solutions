T = int(input())
match = [".", "*", "\\", "+"]

for i in range(T):
    S = input()

    count = 0
    for i in range(len(S)):
        if S[i] != match[i]:
            count += 1

    if count == 0:
        print("True")
    else:
        print("False")
