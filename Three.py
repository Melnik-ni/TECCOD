import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

p1 = Point(1, 2)
p2 = Point(4, 6)
print(p1.distance_to(p2))  # Расстояние между p1 и p2
print(p1.get_coordinates())  # Получение координат точки p1
p1.set_coordinates(3, 4)  # Изменение координат точки p1
print(p1.get_coordinates())  # Получение новых координат точки p1