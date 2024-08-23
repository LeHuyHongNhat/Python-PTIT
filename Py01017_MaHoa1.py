for _ in range(int(input())):
    s = input()
    result = ""
    i = 0
    while i < len(s):
        cnt = 1
        c = s[i]
        for j in range(i + 1, len(s)):
            if s[j] == c:
                cnt += 1
            else:
                break
        i += cnt
        result += str(cnt) + c
    print(result)
