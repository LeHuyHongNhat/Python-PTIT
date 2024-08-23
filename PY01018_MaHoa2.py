p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    inp = input()
    if inp == "0":
        break
    k, s = inp.split()
    result = ""
    for i in s:
        x = p.find(i)
        result += p[(x + int(k)) % 28]
    print(result[::-1])
