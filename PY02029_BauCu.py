def count_elements(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


# Đọc đầu vào
n, m = map(int, input().split())
a = [int(x) for x in input().split()]

# Đếm số phiếu bầu cho mỗi ứng viên
b = count_elements(a)

# Chuyển đổi từ điển thành danh sách các tuple (ứng viên, số phiếu)
b = list(b.items())

# Sắp xếp danh sách theo số phiếu từ cao xuống thấp và theo số thứ tự ứng viên từ bé đến lớn
b = sorted(b, key=lambda x: (-x[1], x[0]))

# Kiểm tra xem có đủ ứng viên để xác định người có số phiếu nhiều thứ hai
if len(b) < 2:
    print("NONE")
else:
    # Tìm số phiếu của ứng viên nhiều phiếu nhất
    highest_vote_count = b[0][1]

    # Tìm ứng viên có số phiếu nhiều thứ hai
    second_highest_candidates = [candidate for candidate in b if candidate[1] < highest_vote_count]

    if not second_highest_candidates:
        print("NONE")
    else:
        second_highest_candidate = second_highest_candidates[0]
        print(second_highest_candidate[0])
