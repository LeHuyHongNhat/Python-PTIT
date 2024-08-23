t = int(input())

a = sorted([int(x) for x in input().split()])
result = max(a[0] * a[1] * a[-1], a[-3] * a[-2] * a[-1])
print(result)
