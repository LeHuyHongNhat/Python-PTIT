def prime_factorization(n):
    factors = []
    d = 2
    while n > 1:
        exp = 0
        while n % d == 0:
            exp += 1
            n //= d
        if exp > 0:
            factors.append((d, exp))
        d += 1
        if d * d > n:
            if n > 1:
                factors.append((n, 1))
            break
    return factors


def format_output(factors):
    result = "1"
    for factor, exp in factors:
        result += f" * {factor}^{exp}"
    return result


t = int(input())

for _ in range(t):
    n = int(input())
    factors = prime_factorization(n)
    print(format_output(factors))
