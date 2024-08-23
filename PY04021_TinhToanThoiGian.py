from datetime import datetime


class GameThur:
    def __init__(self, code, name, start_time, end_time):
        self.code = code
        self.name = name
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.end_time = datetime.strptime(end_time, "%H:%M")
        self.play_time = self.calculate_play_time()

    def calculate_play_time(self):
        delta = self.end_time - self.start_time
        total_minutes = delta.total_seconds() // 60
        return int(total_minutes // 60), int(total_minutes % 60)

    def __str__(self):
        hours, minutes = self.play_time
        return f"{self.code} {self.name} {hours} gio {minutes} phut"


num_gamers = int(input().strip())
gamers = []

for _ in range(num_gamers):
    code = input().strip()
    name = input().strip()
    start_time = input().strip()
    end_time = input().strip()
    gamer = GameThur(code, name, start_time, end_time)
    gamers.append(gamer)

gamers.sort(key=lambda x: (x.play_time[0] * 60 + x.play_time[1]), reverse=True)

for gamer in gamers:
    print(gamer)
