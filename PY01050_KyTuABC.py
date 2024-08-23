def generate_strings(N):
    result = []

    def backtrack(current, a, b, c):
        if len(current) > N:
            return
        if a > 0 and b > 0 and c > 0 and a <= b <= c:
            result.append(''.join(current))
        if len(current) == N:
            return

        backtrack(current + ['A'], a + 1, b, c)
        backtrack(current + ['B'], a, b + 1, c)
        backtrack(current + ['C'], a, b, c + 1)

    backtrack([], 0, 0, 0)
    return sorted(result, key=lambda x: (len(x), x))


N = int(input())

for s in generate_strings(N):
    print(s)

# def Try(s, n, a, b, c) :
# 	if len(s) == n and a <= b and b <= c and a > 0 : print(s)
# 	if len(s) < n :
# 		Try(s + "A", n, a + 1, b, c)
# 		Try(s + "B", n, a, b + 1, c)
# 		Try(s + "C", n, a, b, c + 1)
# n = int(input())
# for i in range(3, n + 1) : Try("", i, 0, 0, 0)
