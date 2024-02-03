from itertools import product

inpA = input()
inpB = input()

A = [int(i) for i in inpA.split(" ")]
B = [int(i) for i in inpB.split(" ")]

for i in product(A, B):
    print(i, end=" ")
print()
