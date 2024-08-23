def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def check_last_four_digits(num):
    # Lấy 4 chữ số cuối cùng
    last_four = num[-4:].zfill(4)

    # Chuyển thành số nguyên
    number = int(last_four)

    # Kiểm tra số nguyên tố
    return is_prime(number)


T = int(input())

for _ in range(T):
    N = input().strip()
    if check_last_four_digits(N):
        print("YES")
    else:
        print("NO")