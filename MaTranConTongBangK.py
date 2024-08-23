import numpy as np


def count_submatrices_with_sum(matrix, K):
    N, M = matrix.shape
    count = 0

    prefix_sum = np.zeros((N + 1, M), dtype=int)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + matrix[i - 1]

    for r1 in range(N):
        for r2 in range(r1, N):
            window_sum = 0
            sum_count = {0: 1}

            for c in range(M):
                window_sum += prefix_sum[r2 + 1, c] - prefix_sum[r1, c]

                if window_sum - K in sum_count:
                    count += sum_count[window_sum - K]

                sum_count[window_sum] = sum_count.get(window_sum, 0) + 1

    return count


T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    matrix = np.array([list(map(int, input())) for _ in range(N)])
    result = count_submatrices_with_sum(matrix, K)
    print(result)