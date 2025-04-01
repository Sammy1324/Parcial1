import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def quadrant(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen."
        elif self.x == 0:
            return "El punto está sobre el eje Y."
        elif self.y == 0:
            return "El punto está sobre el eje X."
        elif self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante."
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante."
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante."
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuarto cuadrante."

    def vector(self, other_point):
        return (other_point.x - self.x, other_point.y - self.y)
    
    def distance(self, other_point):
        other_point = Point(x=int(), y=int())
        distance = math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)
        return distance