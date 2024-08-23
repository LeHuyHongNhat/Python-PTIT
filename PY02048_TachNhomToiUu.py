n, k = map(int, input().split())
a = sorted([int(x) for x in input().split()])
cont = 0
for i in range(0, n - 1):
    a[i] = a[i + 1] - a[i]
for i in a:
    if i > k:
        cont += 1
if cont == 0:
    print(1)
else:
    print(cont)
