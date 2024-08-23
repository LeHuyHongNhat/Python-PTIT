for i in range(int(input())):
    n, x = map(int, input().split())
    a = [int(j) for j in input().split()]
    print(" ".join(map(str, a[x:])), " ".join(map(str, a[:x])))
