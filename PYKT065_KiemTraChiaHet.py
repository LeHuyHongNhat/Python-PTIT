def cnt(l, r, k):
    cont = 0
    is_p = [True] * (r + 1)
    for i in range(2, k + 1):
        if is_p[i]:
            for j in range(i * i, r + 1, i):
                is_p[j] = False

    if l >= k:
        for i in range(l, r + 1):
            if is_p[i]:
                cont += 1
    else:
        for i in range(k + 1, r + 1):
            if is_p[i]:
                cont += 1

    if l == 1:
        cont += 1

    return cont


while True:
    c = input()
    if c == '-1':
        break
    l, r = c.split()
    k = int(input())
    print(cnt(int(l), int(r), k))
