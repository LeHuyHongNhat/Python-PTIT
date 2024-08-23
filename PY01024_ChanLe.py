def check(s):
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i-1])) != 2:
            return False
    su = 0
    for i in s:
        su += int(i)

    if su % 10 != 0:
        return False

    return True


for _ in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")