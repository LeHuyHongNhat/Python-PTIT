def count_ways(n):
    count = 0
    k = 1
    while k * (k + 1) // 2 <= n:
        numerator = n - k * (k - 1) // 2
        if numerator % k == 0:
            a = numerator // k
            if a > 0:
                count += 1
        k += 1
    return count - 1


for _ in range(int(input())):
    N = int(input())
    print(count_ways(N))

