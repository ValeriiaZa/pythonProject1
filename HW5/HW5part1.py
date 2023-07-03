class Point:
    def __init__(self, x, y):
        self.center_x = x
        self.center_y = y

class Circle(Point):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def contains(center_x, cennter_y, x,y, radius):
        if (x-center_x)**2 + (y-cennter_y)**2 <= radius**2:
            return True
        return False


Circle.contains(2, 3, 4, 10, 6)