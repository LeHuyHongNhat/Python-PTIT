def process_number(N):
    even_sum = 0
    odd_product = 1
    all_odd_zero = True

    for i, digit in enumerate(N):
        if i % 2 == 0:  # Vị trí chẵn (bắt đầu từ 0)
            even_sum += int(digit)
        else:  # Vị trí lẻ
            if digit != '0':
                odd_product *= int(digit)
                all_odd_zero = False

    # Nếu tất cả các vị trí lẻ đều là 0
    if all_odd_zero:
        odd_product = 0

    return even_sum, odd_product


T = int(input())

for _ in range(T):
    N = input().strip()
    even_sum, odd_product = process_number(N)
    print(f"{odd_product} {even_sum}")
