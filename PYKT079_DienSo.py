for _ in range(int(input())):
    n = int(input())
    a = set(int(x) for x in input().split())
    x = max(a) - min(a) + 1
    print(x - len(a))
