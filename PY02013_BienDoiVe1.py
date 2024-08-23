def count_collatz_steps(N):
    count = 0
    while N != 1:
        count += 1
        if N % 2 == 0:
            N = N // 2
        else:
            N = 3 * N + 1
    return count + 1  # Thêm 1 vì tính luôn giá trị cuối cùng là 1


def main():
    while True:
        N = int(input().strip())
        if N == 0:
            break
        print(count_collatz_steps(N))


if __name__ == "__main__":
    main()
