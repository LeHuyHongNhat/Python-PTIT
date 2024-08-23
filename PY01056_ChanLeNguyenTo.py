def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def check_number(num):
    total_sum = 0

    for i, digit in enumerate(num, start=1):
        digit = int(digit)
        total_sum += digit

        # Kiểm tra vị trí chẵn là chữ số chẵn
        if i % 2 == 0 and digit % 2 == 0:
            return False

        # Kiểm tra vị trí lẻ là chữ số lẻ
        if i % 2 != 0 and digit % 2 != 0:
            return False

    # Kiểm tra tổng chữ số là số nguyên tố
    return is_prime(total_sum)


T = int(input())

for _ in range(T):
    num = input().strip()
    if check_number(num):
        print("YES")
    else:
        print("NO")