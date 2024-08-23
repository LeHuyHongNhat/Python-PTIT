def is_valid_ipv4(ip):
    # Tách chuỗi thành các phần bằng dấu chấm
    parts = ip.split('.')

    # Kiểm tra xem có đúng 4 phần hay không
    if len(parts) != 4:
        return False

    for part in parts:
        # Kiểm tra xem phần có phải là số nguyên hay không
        if not part.isdigit():
            return False

        # Chuyển đổi sang số nguyên
        num = int(part)

        # Kiểm tra giá trị có nằm trong khoảng 0-255 hay không
        if num < 0 or num > 255:
            return False

        # Kiểm tra số 0 đứng đầu
        if len(part) > 1 and part[0] == '0':
            return False

    return True


T = int(input())

for _ in range(T):
    ip = input().strip()
    if is_valid_ipv4(ip):
        print("YES")
    else:
        print("NO")
