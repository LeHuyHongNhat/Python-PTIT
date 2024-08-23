def generate_fibonacci():
    fib = [0, 1, 1]  
    while len(fib) < 93:
        fib.append(fib[-1] + fib[-2])
    return fib


fibonacci = generate_fibonacci()

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    result = ' '.join(map(str, fibonacci[a:b + 1]))
    print(result)
