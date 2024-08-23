n = int(input())
a = [0] * n
b = []
while True:
    x = [int(x) for x in input().split()]
    b += x
    if len(b) == n:
        break

odd = sorted([i for i in b if i % 2 == 1])
even = sorted([i for i in b if i % 2 == 0], reverse=True)
for i in range(n):
    if b[i] % 2 == 1:
        a[i] = 1
for i in range(n):
    if a[i] == 0:
        print(even[-1], end=' ')
        even.pop()
    else:
        print(odd[-1], end=' ')
        odd.pop()
