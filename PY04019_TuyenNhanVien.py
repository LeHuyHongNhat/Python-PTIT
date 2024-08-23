def categorize(tb):
    if tb < 5:
        return "TRUOT"
    elif tb < 8:
        return "CAN NHAC"
    elif tb <= 9.5:
        return "DAT"
    else:
        return "XUAT SAC"


def chuanhoaDiem(x):
    return x / 10 if x > 10 else x


class nhanVien:
    def __init__(self, id, name, lt, th):
        self.id = id
        self.name = name
        self.lt = chuanhoaDiem(lt)
        self.th = chuanhoaDiem(th)
        self.tb = (self.lt + self.th) / 2
        self.xl = categorize(self.tb)

    def __str__(self):
        return f"{self.id} {self.name} {self.tb:.2f} {self.xl}"


num_stu = int(input())
students = []

for i in range(1, num_stu + 1):
    name = input().strip()
    lt = float(input().strip())
    th = float(input().strip())
    lt = chuanhoaDiem(lt)
    th = chuanhoaDiem(th)
    student = nhanVien(f"TS0{str(i)}", name, lt, th)
    students.append(student)

students.sort(key=lambda x: x.tb, reverse=True)
for student in students:
    print(student)
