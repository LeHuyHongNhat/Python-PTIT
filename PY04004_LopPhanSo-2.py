from math import gcd


class PS:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def rutgon(self):
        tu = self.a * self.d + self.b * self.c
        mau = self.b * self.d
        ucln = gcd(tu, mau)
        return f'{tu // ucln}/{mau // ucln}'


a, b, c, d = map(int, input().split())
p = PS(a, b, c, d)
print(p.rutgon())
