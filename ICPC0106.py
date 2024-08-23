import math

# Danh sách các ký tự dùng để chuyển đổi cơ số
f = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# Đọc số lượng bộ test
t = int(input().strip())

# Đọc và xử lý từng bộ test
for _ in range(t):
    b = int(input().strip())
    a = input().strip()

    # Xác định số bit nhóm lại dựa trên cơ số b
    if b == 2:
        n = 1
    elif b == 4:
        n = 2
    elif b == 8:
        n = 3
    elif b == 16:
        n = 4
    else:
        raise ValueError("Base must be one of 2, 4, 8, 16")

    # Thêm các ký tự '0' vào đầu để đủ số bit nhóm lại
    while len(a) % n != 0:
        a = '0' + a

    # Chuyển đổi từng nhóm n bit sang cơ số b
    result = ""
    for i in range(0, len(a), n):
        s = 0
        for j in range(i, i + n):
            if a[j] == '1':
                s += pow(2, n - j + i - 1)
        result += f[s]

    # In kết quả
    print(result)
