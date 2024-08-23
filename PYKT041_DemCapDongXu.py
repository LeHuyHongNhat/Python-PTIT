n = int(input())
a = []
c = [['' for _ in range(n)] for _ in range(n)]
cnt = 0

for _ in range(n):
    a.append(input())

for i in range(n):
    for j in range(n):
        c[i][j] = a[j][i]

for row in a:
    x = row.count('C')
    cnt += x * (x - 1) / 2

for row in c:
    x = row.count('C')
    cnt += x * (x - 1) / 2

print(int(cnt))
