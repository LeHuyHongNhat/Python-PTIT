def is_valid_base3(s):
    valid_digits = set('012')
    for char in s:
        if char not in valid_digits:
            return False

    return True


t = int(input())

for _ in range(t):
    s = input().strip()
    if is_valid_base3(s):
        print("YES")
    else:
        print("NO")