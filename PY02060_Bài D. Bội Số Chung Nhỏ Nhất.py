from math import isqrt
from sys import stdin, stdout

N, mod = 10 ** 6, 10 ** 9 + 7


def sieve():
    U = list(range(N + 1))
    primes = []
    for i in range(2, N + 1):
        if U[i] == i:
            primes.append(i)
            for j in range(i * i, N + 1, i):
                if U[j] == j:
                    U[j] = i
    return U, primes


U, primes = sieve()

# Precompute powers of 3
POW3 = [1] * (N + 1)
for i in range(1, N + 1):
    POW3[i] = POW3[i - 1] * 3 % mod


def count(x, n):
    result = 0
    while n >= x:
        result += n // x
        n //= x
    return result


input = stdin.read().split()
index = 0
T = int(input[index])
index += 1
output = []

for _ in range(T):
    a = int(input[index])
    b = int(input[index + 1])
    index += 2
    ans = 1

    for p in primes:
        if p > b // 2:
            break
        ans = ans * ((count(p, b) - count(p, a - 1)) * 2 + 1) % mod

    m = sum(1 for p in primes if b // 2 < p <= b)
    ans = ans * POW3[m] % mod
    output.append(str(ans))

stdout.write("\n".join(output) + "\n")
