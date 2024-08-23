def binary_search(arr, left, right, target):
    # Binary search to find the smallest index where arr[index] >= target.
    while left < right:
        mid = (left + right) >> 1
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def find_next_greater_indices(arr, result):
    # Compute the index of the first element greater than each element in 'arr'.
    stack = []
    for i in range(1, len(arr)):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        result[i] = stack[-1] if stack else 0
        stack.append(i)


def main():
    test_cases = int(input())
    data = []

    # Read all inputs
    while True:
        try:
            data.extend(map(int, input().split()))
        except EOFError:
            break

    index = 0
    for _ in range(test_cases):
        n = data[index]
        index += 1

        left_bound = [-1] + data[index:index + n]
        index += n
        heights = [0] + data[index:index + n]
        index += n

        next_greater_index = [0] * (n + 1)
        find_next_greater_indices(heights, next_greater_index)

        Vn = [0] * (n + 2)
        Vw = [0] * (n + 2)

        for i in range(1, n + 1):
            if heights[i] > heights[i - 1]:
                Vn[i] = (Vn[next_greater_index[i]] +
                         heights[i] * (left_bound[i] - left_bound[next_greater_index[i]] - 1) -
                         (Vw[i - 1] - Vw[next_greater_index[i]]))
            else:
                Vn[i] = Vn[i - 1] + heights[i] * (left_bound[i] - left_bound[i - 1] - 1)
            Vw[i] = Vw[i - 1] + heights[i]

        Vn[n + 1] = 10 ** 18
        queries = data[index]
        index += 1

        for _ in range(queries):
            k = data[index]
            index += 1
            print(binary_search(Vn, 1, n + 1, k) - 1)


if __name__ == "__main__":
    main()
