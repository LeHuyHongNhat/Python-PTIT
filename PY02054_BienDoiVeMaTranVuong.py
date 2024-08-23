n, m = map(int, input().split())
matrix = []
for _ in range(n):
    a = [int(x) for x in input().split()]
    matrix.append(a)
k = max(n, m)
if n > m:
    for i in range(k):
        if i % 2 == 0:
            matrix[i] = []
            n -= 1
        if n == m:
            break
    for i in matrix:
        if len(i) != 0:
            print(" ".join(map(str, i)))

elif n < m:
    for i in range(k):
        if i % 2 != 0:
            for j in range(n):
                matrix[j][i] = -100000000000000
            m -= 1
        if n == m:
            break
    for i in range(n):
        for j in range(k):
            if matrix[i][j] != -100000000000000:
                print(matrix[i][j], end=" ")
        print()
# 4 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8

# 11 4
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
# 5 5 5 5
# 6 6 6 6
# 7 7 7 7
# 8 8 8 8
# 9 9 9 9
# 10 10 10 10
# 11 11 11 11
