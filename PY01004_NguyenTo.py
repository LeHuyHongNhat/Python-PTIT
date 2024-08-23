import math


def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return is_prime


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


a = sieve_of_eratosthenes(10000)
for i in range(int(input())):
    n = int(input())
    k = 0
    for j in range(1, n):
        if math.gcd(j, n) == 1:
            k += 1
    # if a[k]:
    if is_prime(k):
        print("YES")
    else:
        print("NO")
