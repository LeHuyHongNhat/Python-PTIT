n = int(input())
matrix = []
for _ in range(n):
    a = [int(x) for x in input().split()]
    matrix.append(a)
k = int(input())
t = 0
d = 0
for i in range(n - 2, -1, -1):
    for j in range(n - 1, i, -1):
        t += matrix[i][j]

for i in range(1, n, 1):
    for j in range(0, i, 1):
        d += matrix[i][j]

kc = abs(t - d)
if kc <= k:
    print("YES")
else:
    print("NO")
print(kc)
