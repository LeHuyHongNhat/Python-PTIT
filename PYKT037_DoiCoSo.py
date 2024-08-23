f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    k = ''
    while a > 0:
        x = a % b
        k += f[x]
        a //= b
    print(k[::-1])
