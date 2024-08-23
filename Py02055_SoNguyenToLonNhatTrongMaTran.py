from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True


def find_max_primes(mtr):
    max_pr = -1
    poss = []

    for i, row in enumerate(mtr):
        for j, value in enumerate(row):
            if is_prime(value):
                if value > max_pr:
                    max_pr = value
                    poss = [(i, j)]
                elif value == max_pr:
                    poss.append((i, j))

    return max_pr, poss


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_prime, positions = find_max_primes(matrix)
if max_prime == -1:
    print('NOT FOUND')
else:
    print(max_prime)
    for pos in positions:
        print(f'Vi tri [{pos[0]}][{pos[1]}]')
