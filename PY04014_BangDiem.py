from decimal import Decimal, ROUND_HALF_UP

def xh(tb):
    if tb >= 9:
        return "XUAT SAC"
    elif tb >= 8:
        return "GIOI"
    elif tb >= 7:
        return "KHA"
    elif tb >= 5:
        return "TB"
    else:
        return "YEU"


def calc(sc):
    return ((sc[0] + sc[1]) * 2 + sum(sc[2:])) / 12


class bd:
    def __init__(self, id, name, sc):
        self.id = id
        self.name = name
        self.sc = sc
        self.tb = (calc(sc)).quantize(Decimal('0.1'), ROUND_HALF_UP)
        self.stt = xh(self.tb)

    def __str__(self):
        return f"{self.id} {self.name} {self.tb:.1f} {self.stt}"


n = int(input())
ds = []
for i in range(1, n + 1):
    ts = bd(f"HS{i:02}", input(), [Decimal(x) for x in input().split()])
    ds.append(ts)
ds.sort(key=lambda x: (-x.tb, x.id))
for x in ds:
    print(x)
