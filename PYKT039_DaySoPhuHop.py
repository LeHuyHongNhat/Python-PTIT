for _ in range(int(input())):
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    k = True
    for i in range(n):
        if a[i] > b[i]:
            k = False
            break
    if k:
        print("YES")
    else:
        print("NO")