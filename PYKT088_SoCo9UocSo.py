import math


def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(limit + 1) if is_prime[i]]


def count_numbers_with_9_divisors(N):
    limit = int(math.sqrt(N)) + 1
    primes = sieve(limit)

    count = 0

    # Count numbers of the form p^8
    for p in primes:
        if p ** 8 <= N:
            count += 1
        else:
            break

    # Count numbers of the form p1^2 * p2^2
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if primes[i] ** 2 * primes[j] ** 2 <= N:
                count += 1
            else:
                break

    return count


N = int(input())

print(count_numbers_with_9_divisors(N))
