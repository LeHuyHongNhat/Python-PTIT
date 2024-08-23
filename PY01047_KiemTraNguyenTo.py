def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def check_last_four_digits(N):
    last_four = N[-4:].zfill(4)

    num = int(last_four)

    return is_prime(num)


t = int(input())

for _ in range(t):
    N = input().strip()
    if check_last_four_digits(N):
        print("YES")
    else:
        print("NO")