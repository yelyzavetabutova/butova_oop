import math

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        p = self.get_perimeter() / 2
        return math.sqrt(max(0, p * (p - self.a) * (p - self.b) * (p - self.c)))

class Rectangle:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def get_perimeter(self):
        return self.a + self.b + self.c + self.d

    def get_area(self):
        diff = abs(self.a - self.b)
        if diff == 0: return 0
        h_sq = self.c ** 2 - (((diff ** 2 + self.c ** 2 - self.d ** 2) / (2 * diff)) ** 2)
        return ((self.a + self.b) / 2) * math.sqrt(max(0, h_sq))

class Parallelogram:
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.h


class Circle:
    def __init__(self, r):
        self.r = r

    def get_perimeter(self):
        return 2 * math.pi * self.r

    def get_area(self):
        return math.pi * self.r ** 2


out = open('output.txt', 'w')

for i in range(1, 4):
    filename = f"input0{i}.txt"
    shapes = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            if not parts: continue

            name, params = parts[0], [float(x) for x in parts[1:]]

            if name == "Triangle":
                shapes.append(Triangle(*params))
            elif name == "Rectangle":
                shapes.append(Rectangle(*params))
            elif name == "Trapeze":
                shapes.append(Trapeze(*params))
            elif name == "Parallelogram":
                shapes.append(Parallelogram(*params))
            elif name == "Circle":
                shapes.append(Circle(*params))

    if shapes:
        m_area = shapes[0]
        m_perim = shapes[0]
        for s in shapes:
            if s.get_area() > m_area.get_area(): m_area = s
            if s.get_perimeter() > m_perim.get_perimeter(): m_perim = s

        out.write(f"File: {filename}\n")
        out.write(f"Max Area: {round(m_area.get_area(), 2)}\n")
        out.write(f"Max Perimeter: {round(m_perim.get_perimeter(), 2)}\n")

out.close()