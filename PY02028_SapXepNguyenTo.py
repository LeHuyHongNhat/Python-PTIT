def soe(num):
    is_prime = [True] * (num + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, num + 1, i):
                is_prime[j] = False
    return is_prime


n = int(input())
a = [int(x) for x in input().split()]
prime = soe(max(a))

b = []
for i in a:
    if prime[i]:
        b.append(i)

b.sort()
k = 0
for idx in range(len(a)):
    if prime[a[idx]]:
        a[idx] = b[k]
        k += 1

for i in a:
    print(i, end=' ')
