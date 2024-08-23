def check(s1):
    s2 = s1[::-1]
    for i in range(len(s1)):
        if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            return False

    return True


for _ in range(int(input())):
    s1 = input()
    if check(s1):
        print("YES")
    else:
        print("NO")
