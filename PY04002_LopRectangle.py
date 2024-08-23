class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self._color = color  # Sử dụng thuộc tính private

    def perimeter(self):
        if self.is_valid():
            return 2 * (self.length + self.width)
        return 0

    def area(self):
        if self.is_valid():
            return self.length * self.width
        return 0

    def color(self):
        if self.is_valid():
            return self._color.capitalize()
        return "INVALID"

    def is_valid(self):
        return self.length > 0 and self.width > 0


arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if r.is_valid():
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")
