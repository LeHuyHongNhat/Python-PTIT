for _ in range(int(input())):
    n = input()
    s = ""
    for i in range(0, len(n), 2):
        s += n[i] * int(n[i + 1])

    print(s)
