def product_of_digits(n):
    product = 1
    for digit in n:
        if digit != '0':
            product *= int(digit)
    return product


T = int(input())

for _ in range(T):
    N = input().strip()  # Đọc N như một chuỗi
    result = product_of_digits(N)
    print(result)
