ip = input()
k = int(input())
A = [int(ip[i:i + 2]) for i in range(0, len(ip) - 1, 2)]
B = {}
for a in A:
    if a not in B:
        B[a] = 1
    else:
        B[a] += 1

C = {}
for num in A:
    if num in B and B[num] >= k:
        C[num] = B[num]
        del B[num]

C_sorted = sorted(C.items())
if len(C) == 0:
    print("NOT FOUND")
else:
    for key, value in C_sorted:
        print(key, value)
