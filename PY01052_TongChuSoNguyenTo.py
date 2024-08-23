def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sum_of_digits(n):
    return sum(int(digit) for digit in n)


T = int(input())

for _ in range(T):
    N = input().strip()
    digit_sum = sum_of_digits(N)
    if is_prime(digit_sum):
        print("YES")
    else:
        print("NO")
