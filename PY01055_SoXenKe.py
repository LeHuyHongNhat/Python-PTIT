def is_alternating(num):
    # Kiểm tra số chữ số là số lẻ
    if len(num) % 2 == 0:
        return False

    # Kiểm tra chữ số đầu tiên khác chữ số thứ hai
    if num[0] == num[1]:
        return False

    # Kiểm tra các số ở vị trí lẻ bằng nhau
    first_digit = num[0]
    for i in range(0, len(num), 2):
        if num[i] != first_digit:
            return False

    return True


T = int(input())

for _ in range(T):
    num = input().strip()
    if is_alternating(num):
        print("YES")
    else:
        print("NO")