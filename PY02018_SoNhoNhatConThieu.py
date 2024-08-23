n = int(input())
a = [int(x) for x in input().split()]
a.sort()
k = 0
for i in range(1, len(a)):
    if a[i] - a[i - 1] != 1:
        k = a[i - 1] + 1
        break

if k == 0:
    print(a[-1] + 1)
else:
    print(k)
