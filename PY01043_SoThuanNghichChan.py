def generate_palindromes(max_n):
    palindromes = []
    for i in range(2, 10, 2):  # Chỉ xét các chữ số chẵn
        palindromes.append(i * 11)  # Số có 2 chữ số

    for i in range(2, 10, 2):
        for j in range(0, 10, 2):
            num = i * 1001 + j * 110
            if num < max_n:
                palindromes.append(num)  # Số có 4 chữ số

    for i in range(2, 10, 2):
        for j in range(0, 10, 2):
            for k in range(0, 10, 2):
                num = i * 100001 + j * 10010 + k * 1100
                if num < max_n:
                    palindromes.append(num)  # Số có 6 chữ số

    return sorted(palindromes)


T = int(input())

all_palindromes = generate_palindromes(1000000)

for _ in range(T):
    N = int(input())
    ans = [num for num in all_palindromes if num < N]
    print(' '.join(map(str, ans)))
