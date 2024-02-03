from itertools import product
from itertools import permutations

# --------------------------- Product -------------------------------
# print(list(product([1, 2, 3], repeat=2)))
# print(list(product([1, 2, 3], [3, 4])))

# A = [[1, 2, 3], [3, 4, 5]]
# print(list(product(*A)))

# B = [[1, 2, 3], [3, 4, 5], [7, 8]]
# print(list(product(*B)))


#  ------------------------Permutation---------------------
# print(list(permutations(['1', '2', '3'])))
# print(list(permutations(['1', '2', '3'], 2)))
print(list(permutations('abc', 3)))

