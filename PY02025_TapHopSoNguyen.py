n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = set(a)
B = set(b)

intersection = sorted(A.intersection(B))

difference_A_B = sorted(A.difference(B))

difference_B_A = sorted(B.difference(A))

print(" ".join(map(str, intersection)) if intersection else "NO")
print(" ".join(map(str, difference_A_B)) if difference_A_B else "NO")
print(" ".join(map(str, difference_B_A)) if difference_B_A else "NO")
