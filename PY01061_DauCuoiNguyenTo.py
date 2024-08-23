def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime_head_tail(num):
    head = int(num[:3])
    tail = int(num[-3:])

    return is_prime(head) and is_prime(tail)


T = int(input())

for _ in range(T):
    N = input().strip()
    if is_prime_head_tail(N):
        print("YES")
    else:
        print("NO")