import math

n, k = map(int, input().split())
idx = 0
for i in range(10 ** (k - 1), 10 ** k):
    if math.gcd(i, n) == 1:
        idx += 1
        print(i, end='')
        if idx % 10 == 0:
            print('', end='\n')
        else:
            print(' ', end='')
