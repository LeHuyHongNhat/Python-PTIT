ip = input()
A = [int(ip[i:i+2]) for i in range(0, len(ip)-1, 2)]
B = {}
for a in range(len(A)):
    if A[a] not in B:
        B[A[a]] = 1
    else:
        B[A[a]] += 1
for num in A:
    if num in B:
        print(f"{num} {B[num]}")
        del B[num]
        