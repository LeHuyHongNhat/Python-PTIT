def zero(row, n):
    return all(val == 0 for val in row)


def solve(a, n):
    # Gaussian elimination
    for i in range(n):
        # Check if the current row is zero and find a non-zero row to swap if needed
        if zero(a[i], n):
            for j in range(i + 1, n):
                if not zero(a[j], n):
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                return -1

        # Make the diagonal element 1
        pivot = a[i][i]
        if pivot == 0:
            return -1

        # Normalize the row
        a[i] = [x / pivot for x in a[i]]

        # Eliminate the column below
        for j in range(i + 1, n):
            factor = a[j][i]
            a[j] = [a[j][k] - factor * a[i][k] for k in range(n + 1)]

    # Back substitution
    ans = [0] * n
    for i in reversed(range(n)):
        s = sum(ans[j] * a[i][j] for j in range(i + 1, n))
        ans[i] = (a[i][-1] - s) / a[i][i]

    return ans


def main():
    T = int(input().strip())

    for _ in range(T):
        n = int(input().strip())

        a = [list(map(int, input().strip().split())) for _ in range(n)]
        b = list(map(int, input().strip().split()))

        for i in range(n):
            a[i].append(b[i])

        ans = solve(a, n)

        if ans == -1:
            print(-1)
        else:
            print(" ".join(f"{x:.3f}" for x in ans))


if __name__ == "__main__":
    main()
