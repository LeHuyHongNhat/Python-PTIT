def check(a, op, b, ans):
    if op == '+':
        return a + b == ans
    if op == '-':
        return a - b == ans
    if op == '*':
        return a * b == ans
    if b != 0 and a % b == 0:
        return a // b == ans
    return False


def genn(a):
    ans = []
    for i in range(10, 100):
        if len(a) == 2 and (a[0] == '?' or a[1] == '?'):
            if (a[0] == '?' or str(i)[0] == a[0]) and (a[1] == '?' or str(i)[1] == a[1]):
                ans.append(str(i))
        elif len(a) == 1 and a == '?':
            ans.append(str(i))
        elif a == str(i):
            ans.append(a)
    return ans


def geno(x):
    if x == '?':
        return ['+', '-', '*', '/']
    return [x]


def solve(s):
    arr = s.split()
    a = genn(arr[0])
    op = geno(arr[1])
    b = genn(arr[2])
    ans = genn(arr[4])
    for i in a:
        for j in op:
            for k in b:
                for m in ans:
                    if check(int(i), j, int(k), int(m)):
                        print(f'{i} {j} {k} = {m}')
                        return
    print('WRONG PROBLEM!')


for t in range(int(input())):
    solve(input())
