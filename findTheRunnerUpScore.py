n = int(input())
mul_inp = list(map(int, input().split()))

if len(mul_inp) == n:
    maxx = max(mul_inp)

    new_list = [i for i in mul_inp if i != maxx]
    print(max(new_list))
    