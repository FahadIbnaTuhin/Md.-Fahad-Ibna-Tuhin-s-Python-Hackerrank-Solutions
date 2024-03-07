# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
from collections import Counter

input()
shoes_quantity = Counter(list(map(int, input().split())))
print(shoes_quantity)

total_price = 0
for _ in range(int(input())):
    size, price = map(int, input().split())
    if size in shoes_quantity and shoes_quantity[size] > 0:
        shoes_quantity[size] -= 1
        total_price += price

print(total_price)


# LESSON
# myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
# print(Counter(myList))
# print(Counter(myList).items())
# print(Counter(myList).keys())
# print(Counter(myList).values())
