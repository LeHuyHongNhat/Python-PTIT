from math import sqrt


def tn(x):
    if len(x) < 2:
        return False
    return x == x[::-1]


def find_max_r(mtr):
    max_pr = -1
    poss = []

    for i, row in enumerate(mtr):
        for j, value in enumerate(row):
            if tn(str(value)):
                if value > max_pr:
                    max_pr = value
                    poss = [(i, j)]
                elif value == max_pr:
                    poss.append((i, j))

    return max_pr, poss


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
max_tn, positions = find_max_r(matrix)
if max_tn == -1:
    print('NOT FOUND')
else:
    print(max_tn)
    for pos in positions:
        print(f'Vi tri [{pos[0]}][{pos[1]}]')
