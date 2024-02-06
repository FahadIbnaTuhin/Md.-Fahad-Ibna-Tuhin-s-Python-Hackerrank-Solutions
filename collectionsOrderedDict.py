N = int(input())

if 0 < N <= 100:
    basket = {}
    for i in range(N):
        inp = input().split()
        item_name = " ".join(inp[:len(inp) - 1])
        net_price = int(inp[len(inp) - 1])
        # print(item_name, net_price)
        if item_name not in basket:
            basket[item_name] = net_price
        else:
            basket[item_name] += net_price
    for key in basket:
        print(key, basket[key])
# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
