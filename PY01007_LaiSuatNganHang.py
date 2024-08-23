def money(gui, lai, thu):
    nam = 0
    while gui < thu:
        gui *= (1 + lai / 100)
        nam += 1
    return nam


t = int(input())
for _ in range(t):
    a, b, c = map(float, input().split())
    print(money(a, b, c))
