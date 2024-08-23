from itertools import combinations

N, K = map(int, input().split())
names = input().split()

# Loại bỏ các tên trùng lặp và sắp xếp theo thứ tự từ điển
unique_names = sorted(set(names))

# Tạo tất cả các tổ hợp K tên từ danh sách tên duy nhất
combinations_list = list(combinations(unique_names, K))

# Sắp xếp các tên trong mỗi tổ hợp và sắp xếp các tổ hợp
sorted_combinations = [tuple(sorted(comb)) for comb in combinations_list]
sorted_combinations.sort()

for comb in sorted_combinations:
    print(' '.join(comb))