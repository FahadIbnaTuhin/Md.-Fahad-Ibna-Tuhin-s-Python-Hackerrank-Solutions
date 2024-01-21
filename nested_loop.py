def second_lowest(a_list):
    new_list = [i for i in a_list if i != min(a_list)]
    return min(new_list)


records = {}
for _ in range(int(input())):
    name = input().title()
    score = float(input())
    records[name] = score
# print(records)

# records = {'Harry': 37.21, 'Berry': 37.21, 'Tina': 37.2, 'Akriti': 41, 'Harsh': 39}

scores = [value for (key, value) in records.items()]
sl = second_lowest(scores)
# print(sl)

names = [key for key, value in records.items() if value == sl]
sorted_names = sorted(names)

for name in sorted_names:
    print(name)
