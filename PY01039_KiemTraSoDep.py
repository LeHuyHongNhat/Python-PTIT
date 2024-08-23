def is_beautiful_number(n):
    s = str(n)

    first_digit = s[0]
    second_digit = s[1]

    # Kiểm tra xem có đúng hai chữ số khác nhau không
    if len(set(s)) != 2:
        return False

    # Kiểm tra tính chất "cách nhau 2 vị trí đều bằng nhau"
    for i in range(0, len(s), 2):
        if s[i] != first_digit:
            return False

    for i in range(1, len(s), 2):
        if s[i] != second_digit:
            return False

    return True


t = int(input())

for _ in range(t):
    n = int(input())
    if is_beautiful_number(n):
        print("YES")
    else:
        print("NO")