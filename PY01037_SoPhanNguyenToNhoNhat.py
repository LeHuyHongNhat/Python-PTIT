def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count


def generate_anti_primes(limit):
    anti_primes = [1]
    max_divisors = 1
    for n in range(2, limit + 1):
        div_count = count_divisors(n)
        if div_count > max_divisors:
            anti_primes.append(n)
            max_divisors = div_count
    return anti_primes


# Tạo danh sách số phản nguyên tố đến 10^7
anti_primes = generate_anti_primes(10 ** 7)

T = int(input())

for _ in range(T):
    X = int(input())
    # Tìm số phản nguyên tố nhỏ nhất không nhỏ hơn X
    result = next(ap for ap in anti_primes if ap >= X)
    print(result)
