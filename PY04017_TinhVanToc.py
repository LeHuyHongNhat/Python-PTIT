class Race:
    def __init__(self, name, unit, time):
        name_initials = ''.join([word[0] for word in name.split()])
        unit_initials = ''.join([word[0] for word in unit.split()])
        self.id = unit_initials + name_initials
        self.name = name
        self.unit = unit
        hours, minutes = map(int, time.split(':'))
        self.speed = 120 / (hours - 6 + minutes / 60)

    def __str__(self):
        return f"{self.id} {self.name} {self.unit} {round(self.speed)} Km/h"


n = int(input())
racers = [Race(input(), input(), input()) for _ in range(n)]
racers = sorted(racers, key=lambda racer: -racer.speed)
print(*racers, sep='\n')
