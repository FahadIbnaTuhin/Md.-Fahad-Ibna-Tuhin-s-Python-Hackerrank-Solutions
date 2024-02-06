from collections import namedtuple

# Pointer = namedtuple('Pointer', 'x y')
# # print(Pointer)
# pt1 = Pointer(1, 2)
# pt2 = Pointer(3, 4)
# # print(pt1)
# dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
# print(dot_product)

Car = namedtuple('Car', 'Price Mileage Color Class')
print(Car)
xyz = Car(Price=10000, Mileage=30, Color='Cyan', Class='A')

print(xyz)
# print(type(xyz))
print(xyz.Color)

