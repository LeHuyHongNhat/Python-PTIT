n = int(input())
a = []
for i in range(n):
    b = input().split()
    a.append(len(b))
c = []
k = 0
while k < n:
    x = 0
    if a[k] % 2 == 0:
        c.append(1)
        while k < n and a[k] % 2 == 0:
            k += 1
    else:
        c.append(2)
        while k < n and a[k] % 2 == 1 and x < 4:
            x += 1
            k += 1
print(len(c))
for i in c:
    print(i)
