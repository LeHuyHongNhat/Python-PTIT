t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(int(x) for x in input().split())
    cnt = 0
    for i in range(0, n - 2):
        left = i + 1
        right = n - 1
        x = a[i]
        while left < right:
            if a[left] + a[right] + x == 0:
                cnt += 1
                left += 1
            elif a[left] + a[right] + x < 0:
                left += 1
            else:
                right -= 1
    print(cnt)


