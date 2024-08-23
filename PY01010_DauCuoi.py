for _ in range(int(input())):
    n = input()
    if n[0] == n[-2] and n[1] == n[-1]:
        print("YES")
    else:
        print("NO")