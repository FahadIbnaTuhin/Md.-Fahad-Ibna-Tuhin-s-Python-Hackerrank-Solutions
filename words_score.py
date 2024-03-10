input()
inp = input().split()

total = 0
for word in inp:
    vowel_count = sum(1 for i in word if i.lower() in "aeiouy")
    total += 2 if vowel_count % 2 == 0 else 1
    # if vowel_count % 2 == 0:
    #     total += 2
    # else:
    #     total += 1

print(total)
