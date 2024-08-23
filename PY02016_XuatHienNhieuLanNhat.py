for _ in range(int(input())):
    n = int(input())
    d = dict()
    for i in map(int, input().split()):
        d[i] = d.get(i, 0) + 1

    flag = False
    for i in d:
        if d[i] > n // 2:
            print(i)
            flag = True
            break

    if not flag:
        print("NO")
