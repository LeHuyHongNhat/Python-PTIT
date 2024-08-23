def digit_product(num):
    product = 1
    for digit in str(num):
        product *= int(digit)
    return product


def sort_by_digit_product(arr):
    return sorted(arr, key=lambda x: (digit_product(x), x))


for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    sorted_A = sort_by_digit_product(A)
    print(' '.join(map(str, sorted_A)))
