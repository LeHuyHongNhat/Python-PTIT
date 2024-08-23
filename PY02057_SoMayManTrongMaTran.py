n, m = map(int, input().split())
a = []
Max = -float('inf')
Min = float('inf')

for _ in range(n):
    arr = list(map(int, input().split()))
    Max = max(Max, max(arr))
    Min = min(Min, min(arr))
    a.append(arr)
diff = Max - Min
pos = [f'Vi tri [{i}][{j}]'
       for i in range(n)
       for j in range(m)
       if a[i][j] == diff]

if not pos:
    print('NOT FOUND')
else:
    print(diff)
    print('\n'.join(pos))
