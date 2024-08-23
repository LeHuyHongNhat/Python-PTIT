MOD = 1000000007


def sum_of_rows(x, m):
    """Tính tổng của các phần tử trong hàng x dựa trên công thức."""
    return (m * x + m * (x - 1) + 1) * m // 2 % MOD


def sum_of_columns(x, n, m):
    """Tính tổng của các phần tử trong cột x dựa trên công thức."""
    return (n * x + m * ((n - 1) * n // 2)) % MOD


def main():
    n, m, k = map(int, input().split())

    # Tạo các từ điển để lưu trữ các cập nhật hàng và cột
    row_updates = {}
    col_updates = {}

    # Xử lý từng cập nhật
    for _ in range(k):
        c, x, y = input().split()
        x = int(x)
        y = int(y)
        if c == 'R':  # Cập nhật hàng
            if x not in row_updates:
                row_updates[x] = y
            else:
                row_updates[x] = (row_updates[x] * y) % MOD
        else:  # c == 'C', cập nhật cột
            if x not in col_updates:
                col_updates[x] = y
            else:
                col_updates[x] = (col_updates[x] * y) % MOD

    # Khởi tạo tổng ban đầu
    total_sum = (n * m + 1) * n * m // 2 % MOD

    # Thêm các đóng góp từ các cập nhật hàng
    for row in row_updates:
        total_sum += sum_of_rows(row, m) * (row_updates[row] - 1)
        total_sum %= MOD

    # Thêm các đóng góp từ các cập nhật cột
    for col in col_updates:
        total_sum += sum_of_columns(col, n, m) * (col_updates[col] - 1)
        total_sum %= MOD

    # Điều chỉnh cho các phần giao nhau giữa cập nhật hàng và cột
    for row in row_updates:
        for col in col_updates:
            x = (row - 1) * m + col
            total_sum = (total_sum - x * (row_updates[row] + col_updates[col] - 1) + x * row_updates[row] * col_updates[
                col]) % MOD

    # Đảm bảo kết quả không âm
    total_sum = (total_sum + MOD) % MOD

    print(total_sum)


if __name__ == "__main__":
    main()
