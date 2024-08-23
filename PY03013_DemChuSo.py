def count_digit(x, n):
    count = 0
    for i in range(10):
        place_value = 10 ** i
        if place_value > n:
            break

        quotient, remainder = divmod(n, place_value)
        current_digit = quotient % 10

        if current_digit > x:
            count += (quotient // 10 + 1) * place_value
        elif current_digit == x:
            count += (quotient // 10) * place_value + (remainder + 1)
        else:
            count += (quotient // 10) * place_value

        if x == 0:
            count -= place_value

    return count


def digits_count_range(digit, low, high):
    return count_digit(digit, high) - count_digit(digit, low - 1)


def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        result = [digits_count_range(i, a, b) for i in range(10)]
        print(*result)


if __name__ == "__main__":
    main()