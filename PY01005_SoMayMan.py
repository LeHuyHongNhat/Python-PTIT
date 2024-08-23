def lucky(s):
    four = 0
    seven = 0
    for i in s:
        if i == '4':
            four += 1
        elif i == '7':
            seven += 1
    return four + seven == 4 or four + seven == 7


n = input()
print('YES' if lucky(n) else 'NO')
