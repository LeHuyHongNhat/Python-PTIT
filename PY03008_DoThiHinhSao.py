n = int(input())
a = {str(i + 1): 0 for i in range(n)}
for i in range(n - 1):
    x, y = input().split()
    a[x] += 1
    a[y] += 1
cnt = 0
for i in a:
    if a[i] == 1:
        cnt += 1
    else:
        cnt += 0
if cnt == n - 1:
    print('Yes')
else:
    print('No')
