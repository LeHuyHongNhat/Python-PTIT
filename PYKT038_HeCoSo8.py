n = input()
if len(n) % 3 != 0:
    n = (3 - len(n) % 3) * '0' + n
k = ''
for i in range(len(n) - 1, 0, -3):
    x = int(n[i]) * 1 + int(n[i - 1]) * 2 + int(n[i - 2]) * 4
    k = str(x) + k
print(k)
