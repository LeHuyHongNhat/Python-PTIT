import math


for _ in range(int(input())):
    n = input()
    reverse_n = n[::-1]
    if math.gcd(int(n), int(reverse_n)) == 1:
        print("YES")
    else:
        print("NO")