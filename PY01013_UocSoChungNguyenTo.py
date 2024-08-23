import math


def soe(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return is_prime


is_p = soe(1000000)

t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    c = math.gcd(a, b)
    s = 0
    while c > 0:
        s += c % 10
        c //= 10
    if is_p[s]:
        print("YES")
    else:
        print("NO")
