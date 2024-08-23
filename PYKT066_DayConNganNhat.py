import math


def find_min_subarray_with_gcd_k(A, N, K):
    min_length = float('inf')
    for i in range(N):
        current_gcd = 0
        for j in range(i, N):
            current_gcd = math.gcd(current_gcd, A[j])
            if current_gcd == K:
                min_length = min(min_length, j - i + 1)
                break  # Không cần kiểm tra thêm vì độ dài sẽ chỉ tăng thêm
    return min_length if min_length != float('inf') else -1


def main():
    import sys
    ip = sys.stdin.read
    data = ip().split()

    index = 0
    T = int(data[index])
    index += 1
    results = []

    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        A = list(map(int, data[index:index + N]))
        index += N

        results.append(find_min_subarray_with_gcd_k(A, N, K))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
