for _ in range(int(input())):
    s = input()
    arr = []
    sum_s = 0
    for i in s:
        if i.isnumeric():
            sum_s += int(i)
        else:
            arr.append(i)
    arr.sort()
    print("".join(arr) + str(sum_s))
