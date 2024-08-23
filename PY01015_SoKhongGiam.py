def non_decreasing(s):
    for i in range(1, len(s) + 1, 1):
        if int(s[i]) < int(s[i - 1]):
            return False

    return True


t = int(input())
for _ in range(t):
    n = input()
    if non_decreasing(n):
        print("YES")
    else:
        print("NO")
