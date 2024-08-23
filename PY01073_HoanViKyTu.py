from itertools import permutations

S = input()

all_permutations = [''.join(p) for p in permutations(S)]

for perm in all_permutations:
    print(perm)
