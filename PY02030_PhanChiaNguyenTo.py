import math


def nt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
a = [int(x) for x in input().split()]

# Tạo dãy B[] từ dãy A[] bằng cách loại bỏ các giá trị bị lặp lại và giữ thứ tự xuất hiện
b = []
seen = set()
for value in a:
    if value not in seen:
        b.append(value)
        seen.add(value)

found = False
for i in range(len(b)):
    sumT = sum(b[:i + 1])
    sumS = sum(b[i + 1:])
    if nt(sumT) and nt(sumS):
        print(i)
        found = True
        break

if not found:
    print("NOT FOUND")
