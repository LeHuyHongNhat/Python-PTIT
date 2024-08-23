def convert_to_band(correct_answers):
    if correct_answers >= 39:
        return 9.0
    elif correct_answers >= 37:
        return 8.5
    elif correct_answers >= 35:
        return 8.0
    elif correct_answers >= 33:
        return 7.5
    elif correct_answers >= 30:
        return 7.0
    elif correct_answers >= 27:
        return 6.5
    elif correct_answers >= 23:
        return 6.0
    elif correct_answers >= 20:
        return 5.5
    elif correct_answers >= 16:
        return 5.0
    elif correct_answers >= 13:
        return 4.5
    elif correct_answers >= 10:
        return 4.0
    elif correct_answers >= 7:
        return 3.5
    elif correct_answers >= 5:
        return 3.0
    elif correct_answers >= 3:
        return 2.5
    else:
        return 2.0


def round_overall(score):
    whole = int(score)
    decimal = score - whole
    if decimal < 0.25:
        return whole
    elif decimal < 0.75:
        return whole + 0.5
    else:
        return whole + 1.0


T = int(input())

for _ in range(T):
    reading, listening, speaking, writing = map(float, input().split())

    # Chuyển đổi điểm Reading và Listening
    reading_band = convert_to_band(int(reading))
    listening_band = convert_to_band(int(listening))

    # Tính điểm trung bình
    average = (reading_band + listening_band + speaking + writing) / 4

    # Làm tròn điểm overall
    overall = round_overall(average)

    print(f"{overall:.1f}")
