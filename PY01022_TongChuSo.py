def sum_n(x):
    s = 0
    for i in x:
        s += ord(i) - ord('0')
    return str(s)


n = input()
cnt = 0
while len(n) > 1:
    n = sum_n(n)
    cnt += 1

print(cnt)
