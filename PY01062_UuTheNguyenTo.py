def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime_digit(d):
    return d in {'2', '3', '5', '7'}


def is_prime_dominant(num):
    length = len(num)

    # Kiểm tra điều kiện 1: số chữ số là số nguyên tố
    if not is_prime(length):
        return False

    prime_count = sum(1 for digit in num if is_prime_digit(digit))
    non_prime_count = length - prime_count

    # Kiểm tra điều kiện 2: số lượng chữ số nguyên tố nhiều hơn
    return prime_count > non_prime_count


T = int(input())

for _ in range(T):
    N = input().strip()
    if is_prime_dominant(N):
        print("YES")
    else:
        print("NO")