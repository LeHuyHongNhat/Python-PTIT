def digit_sum(num):
    return sum(int(digit) for digit in str(num))


def sort_by_digit_sum(arr):
    return sorted(arr, key=lambda x: (digit_sum(x), x))


T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    sorted_A = sort_by_digit_sum(A)
    print(' '.join(map(str, sorted_A)))
