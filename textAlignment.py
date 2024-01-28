thickness = int(input())
c = "H"

for i in range(thickness):
    print((c*i).rjust(thickness - 1, "_")+c+(c*i).ljust(thickness - 1, "_"))

for i in range(thickness + 1):
    print((c*thickness).center(thickness*2, "_")+(c*thickness).center(6*thickness, "_"))

for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6, "_"))

for i in range(thickness + 1):
    print((c*thickness).center(thickness*2, "_")+(c*thickness).center(6*thickness, "_"))

for i in range(5):
    print(((c*(thickness - i - 1)).rjust(thickness, "_")+c+(c * (thickness - i - 1))
           .ljust(thickness, "_")).rjust(thickness * 6, "_"))
