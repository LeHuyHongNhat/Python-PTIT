from itertools import combinations


def generate_combinations(k, a):
    unique_sorted_A = sorted(set(a))

    for combo in combinations(unique_sorted_A, k):
        print(' '.join(map(str, combo)))


N, K = map(int, input().split())
A = list(map(int, input().split()))

generate_combinations(K, A)
