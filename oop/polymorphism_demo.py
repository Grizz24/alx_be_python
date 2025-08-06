import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
class Rectangle(Shape):
    def __init__(self, length : int, width : int):
        self.length = length
        self.width = width

    def area(self):
        area_rectangle = self.length * self.width
        print(f"The area of the Rectangle is: {area_rectangle}")
    
class Circle(Shape):
    def __init__(self, radius : float):
        self.radius = radius

    def area(self):
        area_circle = math.pi * self.radius ** 2
        print(f"The area of the Circle is: {area_circle}")
