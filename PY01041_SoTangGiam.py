def check(s):
    if len(s) < 3:
        return False

    dinh = -1
    for i in range(1, len(s)):
        if int(s[i]) > int(s[i - 1]):
            dinh = i
        else:
            break
    for i in range(dinh + 1, len(s)):
        if int(s[i - 1]) < int(s[i]):
            return False

    return True


for _ in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
