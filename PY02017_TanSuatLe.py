def find_odd_occurrence(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(find_odd_occurrence(A))
