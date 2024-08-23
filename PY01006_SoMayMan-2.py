def luckyNumber(s):
    for i in s:
        if int(i) != 4 and int(i) != 7:
            return False
    return True


t = int(input())
for _ in range(t):
    s = input()
    if luckyNumber(s):
        print("YES")
    else:
        print("NO")
