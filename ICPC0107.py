def min_max_sum(p, q, X1, X2):
    m = min(q, p)
    n = max(q, p)
    min_sum = int(X1.replace(n, m)) + int(X2.replace(n, m))
    max_sum = int(X1.replace(m, n)) + int(X2.replace(m, n))

    return min_sum, max_sum


# Đọc và xử lý từng bộ test
for _ in range(int(input())):
    p, q = input().split()
    X1 = input().strip()
    if X1.count(' '):
        X1, X2 = X1.split()
    else:
        X2 = input()

    min_sum, max_sum = min_max_sum(p, q, X1, X2)
    print(min_sum, max_sum)
