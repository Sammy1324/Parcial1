from Point import Point

class Rectangle:
    def __init__(self, initial_point=None, final_point=None):
        self.initial_point = initial_point if initial_point else Point(0, 0)
        self.final_point = final_point if final_point else Point(0, 0)

    def basis(self):
        return abs(self.final_point.x - self.initial_point.x)

    def height(self):
        return abs(self.final_point.y - self.initial_point.y)

    def area(self):
        return self.basis() * self.height()