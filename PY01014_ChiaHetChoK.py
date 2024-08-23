import math

a, K, N = map(int, input().split())
du = a % K
b = K - du
N -= N % K + a
if du == 0 and a + b <= N:
    for i in range(K, N + K, K):
        print(i, end=' ')
elif du != 0 and a + b <= N:
    for i in range(b, N + K, K):
        print(i, end=' ')
else:
    print(-1)
