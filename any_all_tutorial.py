# This expression returns True if any element of the iterable is true.
# If the iterable is empty, it will return False.

print(any([1 > 0, 1 == 0, 1 < 0]))

# This expression returns True if all of the elements of the iterable are true. If the iterable is empty,
# it will return True.
print(all(['a' < 'b', 'b' < 'c']))
print(all(['a' < 'b', 'c' < 'b']))
