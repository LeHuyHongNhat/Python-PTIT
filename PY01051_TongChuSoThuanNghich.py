def sum_of_digits(n):
    return sum(int(digit) for digit in n)


def is_palindrome(n):
    return str(n) == str(n)[::-1] and n > 9


T = int(input())

for _ in range(T):
    N = input().strip()  # Đọc N như một chuỗi
    digit_sum = sum_of_digits(N)
    if is_palindrome(digit_sum):
        print("YES")
    else:
        print("NO")
