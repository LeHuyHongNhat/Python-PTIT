from itertools import permutations


def generate_permutations(n):
    numbers = ''.join(map(str, range(1, n + 1)))
    perms = sorted([''.join(p) for p in permutations(numbers)], reverse=True)
    return perms


for _ in range(int(input())):
    N = int(input())
    result = generate_permutations(N)
    print(len(result))
    print(' '.join(result))