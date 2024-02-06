a = input()
# 5 4 3 2
lis = a.split()
print (lis)
# ['5', '4', '3', '2']

newlis = list(map(int, lis))
print (newlis)
# [5, 4, 3, 2]

myset = {1, 2} # Directly assigning values to a set
myset = set()  # Initializing a set
# myset = set(['a', 'b']) # Creating a set from a list
# myset
# {'a', 'b'}

myset.add('c')
# myset
# {'a', 'c', 'b'}
myset.add('a') # As 'a' already exists in the set, nothing happens
myset.add((5, 4))
# myset
# {'a', 'c', 'b', (5, 4)}

myset.update([1, 2, 3, 4]) # update() only works for iterable objects
# myset
# {'a', 1, 'c', 'b', 4, 2, (5, 4), 3}
myset.update({1, 7, 8})
# myset
# {'a', 1, 'c', 'b', 4, 7, 8, 2, (5, 4), 3}
myset.update({1, 6}, [5, 13])
# myset
# {'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}

myset.discard(10)
# myset
# {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
myset.remove(13)
# myset
# {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3}

a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
a.union(b) # Values which exist in a or b
# {2, 4, 5, 9, 11, 12}
a.intersection(b) # Values which exist in a and b
# {2, 4}
a.difference(b) # Values which exist in a but not in b
# {9, 5}

# a.union(b) == b.union(a)
# True
# a.intersection(b) == b.intersection(a)
# True
# a.difference(b) == b.difference(a)
# False