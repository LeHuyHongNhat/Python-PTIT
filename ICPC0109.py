import sys
import heapq
import re

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    line = ' ' + input().replace(' ', '  ') + ' '
    a = []
    i = -8  # -10^8
    ans = 0
    while i < 9 and len(a) < 4:
        s = '\d' * abs(i) + ' '
        if i < 0:
            s = '-' + s
        elif i > 0:
            s = ' ' + s
        else:
            i += 1
            continue
        a += [int(x) for x in re.findall(s, line)]
        i += 1

    for x in heapq.nsmallest(3, a):
        ans += x
    print(ans)
