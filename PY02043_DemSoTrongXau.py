t = int(input())
for _ in range(t):
    n = input()
    k = input()
    i = 0
    cnt = 0
    while i < len(n):
        if n[i:i+len(k)] == k:
            cnt += 1
            i += len(k)
        else:
            i += 1
    print(cnt)
