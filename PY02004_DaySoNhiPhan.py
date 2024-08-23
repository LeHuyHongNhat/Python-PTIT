N = int(input())
a = [int(x) for x in input().split()]
cnt = 0
for i in range(1, len(a)):
    if a[i - 1] != a[i]:
        cnt += 1
print(cnt)
