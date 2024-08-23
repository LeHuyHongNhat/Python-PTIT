sum_rows = []
n = int(input())
for i in range(n):
    row = [int(x) for x in input().split()]
    sum_row = sum(row)
    sum_rows.append(sum_row)
sum_all = sum(sum_rows) / (2 * (n - 1))
for i in range(n):
    print(int((sum_rows[i] - sum_all) / (n - 2)), end=' ')

