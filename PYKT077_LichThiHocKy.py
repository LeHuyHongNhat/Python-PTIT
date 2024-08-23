import datetime


def main():
    n, m = map(int, input().strip().split())

    subjects = {input().strip(): input().strip() for _ in range(n)}

    exam_slots = []
    for i in range(1, m + 1):
        subject_code, date, time, group = input().strip().split()
        exam_id = f"T{i:03d}"
        subject_name = subjects[subject_code]
        exam_date = datetime.datetime.strptime(date, "%d/%m/%Y")
        exam_time = datetime.datetime.strptime(time, "%H:%M").time()
        exam_slots.append((exam_id, subject_code, subject_name, exam_date, exam_time, group))

    exam_slots.sort(key=lambda x: (x[3], x[4], x[1]))

    for slot in exam_slots:
        date_str = slot[3].strftime("%d/%m/%Y")
        time_str = slot[4].strftime("%H:%M")
        print(f"{slot[0]} {slot[1]} {slot[2]} {date_str} {time_str} {slot[5]}")


if __name__ == "__main__":
    main()
