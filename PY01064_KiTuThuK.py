def find_char(N, K):
    if N == 1:
        return 'A'
    mid = 2**(N-1)
    if K == mid:
        return chr(ord('A') + N - 1)
    elif K < mid:
        return find_char(N-1, K)
    else:
        return find_char(N-1, K-mid)


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(find_char(N, K))
