t = int(input())
a = []

for i in range(t):
    x = input()
    a.append(x)

k = 0
while k < len(a):
    x = ''
    cont = 0
    if a[k] != '':
        x = a[k]
        k += 1
    else:
        k += 1
        continue
    for i in range(k, len(a)):
        if a[i] != '':
            cont += 1
            k += 1
        else:
            break
    print(f'{x}: {cont}')


