def reverse_number(n):
    return int(str(n)[::-1])


def find_divisible_by_seven(n):
    for _ in range(1000):
        if n % 7 == 0:
            return n
        n += reverse_number(n)
    return -1


t = int(input())

for _ in range(t):
    n = int(input())
    result = find_divisible_by_seven(n)
    print(result)
