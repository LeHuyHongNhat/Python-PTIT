def sieve_of_eratosthenes(n):
    # Create a list from 1 to n == True
    is_prime = [True] * (n + 1)
    # 0 and 1 are not prime numbers, so set them as False
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False  # set "non" prime numbers as False

    return is_prime


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

primes = sieve_of_eratosthenes(1000)

result = [[1 if primes[num] else 0 for num in row] for row in matrix]

for row in result:
    print(*row)  # print result following each line
