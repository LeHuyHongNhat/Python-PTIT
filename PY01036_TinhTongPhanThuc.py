def calculate_sum(N):
    if N % 2 == 1:
        return sum(1 / i for i in range(1, N + 1, 2))
    else:
        return sum(1 / i for i in range(2, N + 1, 2))


T = int(input())

for _ in range(T):
    N = int(input())
    result = calculate_sum(N)
    print(f"{result:.6f}")
