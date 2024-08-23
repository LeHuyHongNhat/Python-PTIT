for j in range(int(input())):
    a = sorted(input())
    b = sorted(input())
    if a == b:
        print(f"Test " + str(j + 1) + ": " + "YES")
    else:
        print(f"Test {j + 1}: " + "NO")
