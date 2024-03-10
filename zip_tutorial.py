# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# Column changed using zip
# for i in zip(a, b):
#     print(i)

# If any column has anything extra, then it will be ignored
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

for i in zip(a, b):
    print(i)
