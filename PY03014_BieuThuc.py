def process(e):
    stack = []
    cn = 1
    result = []
    for c in e:
        if c == '(':
            stack.append(cn)
            result.append(cn)
            cn += 1
        elif c == ')':
            openN = stack.pop()
            result.append(openN)
    return ' '.join(map(str, result))


t = int(input())
for i in range(t):
    e = input()
    print(process(e))