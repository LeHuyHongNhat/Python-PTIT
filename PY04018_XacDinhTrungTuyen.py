class Teacher:
    PRIORITY_SCORES = {
        '1': 2.0,
        '2': 1.5,
        '3': 1.0,
        '4': 0.0
    }
    SUBJECTS = {
        'A': 'TOAN',
        'B': 'LY',
        'C': 'HOA'
    }

    def __init__(self, name, code, cs_score, spec_score, index):
        self.name = name
        self.subject = self.SUBJECTS[code[0]]
        self.priority_score = self.PRIORITY_SCORES[code[1]]
        self.total_score = cs_score * 2 + spec_score + self.priority_score
        self.result = "TRUNG TUYEN" if self.total_score >= 18 else "LOAI"
        self.teacher_id = f"GV{index:02d}"

    def __str__(self):
        return f"{self.teacher_id} {self.name} {self.subject} {self.total_score:.1f} {self.result}"


n = int(input())
teachers = []

for i in range(1, n + 1):
    name = input().strip()
    code = input().strip()
    cs_score = float(input().strip())
    spec_score = float(input().strip())
    teachers.append(Teacher(name, code, cs_score, spec_score, i))

teachers = sorted(teachers, key=lambda teacher: -teacher.total_score)

for teacher in teachers:
    print(teacher)
