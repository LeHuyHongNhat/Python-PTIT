n = input()
while len(n) > 1:
    a = n[:len(n)//2]
    b = n[len(n)//2:]
    n = str(int(a) + int(b))
    print(n)
