from math import gcd


class PS:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        self.gcd = gcd(tu, mau)

    def rutgon(self):
        self.tu //= self.gcd
        self.mau //= self.gcd
        return f'{self.tu}/{self.mau}'


tu, mau = map(int, input().split())
p = PS(tu, mau)
print(p.rutgon())


