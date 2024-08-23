def soe(k):
    is_prime = [True] * (k + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(k ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, k + 1, i):
                is_prime[j] = False

    return is_prime


is_prime = soe(1000000)
n = int(input())
a = [int(i) for i in input().split()]
b = {}
for i in a:
    if is_prime[i]:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
for i in b:
    print(i, b[i])
