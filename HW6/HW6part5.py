import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point(self):
        return (self.x, self.y)


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.points = self.generate_points()

    def generate_points(self):
        points = []
        for i in range(self.x - self.radius, self.x + self.radius):
            for j in range(self.y - self.radius, self.y + self.radius):
                if math.sqrt((i - self.x)**2 + (j - self.y)**2) <= self.radius**2:
                    points.append((i, j))
        return points


point = Point(0, 9)
circle = Circle(0, 0, 10)

print(point.point() in circle.points)