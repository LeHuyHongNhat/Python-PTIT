# Hàm xử lý thông báo
def process_notification(notif):
    words = notif.split()
    result = []
    current_length = 0

    for word in words:
        if current_length + len(word) + (len(result) > 0) <= 100:
            result.append(word)
            current_length += len(word) + 1  # Cộng thêm 1 cho khoảng trắng giữa các từ
        else:
            break

    return ' '.join(result)


T = int(input())

for _ in range(T):
    notification = input()
    print(process_notification(notification))
