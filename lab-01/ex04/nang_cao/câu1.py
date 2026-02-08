from itertools import permutations

lst = [1, 2, 3]

print("Các hoán vị của [1, 2, 3]:")
for p in permutations(lst):
    print(p)
