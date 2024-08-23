st = [0] * 500500
cnt = [0] * 500500
res = 0
last = 0
n = int(input())
for i in range(1, n + 1):
    x = int(input())
    j = 0
    s = 0
    while last > 0 and st[last] <= x:
        j += cnt[last]
        if st[last] == x:
            s = 1
        last -= 1
    if st[last] > x:
        j += 1
    if i > 1:
        res += j
    if s == 0:
        last += 1
        st[last] = x
        cnt[last] = 1
    else:
        last += 1
        cnt[last] += 1
print(res)
