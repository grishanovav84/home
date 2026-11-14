import abc
class Shape(abc.ABC):
    @abc.abstractmethod 
    def area (self): pass       # площадь фигуры
 
# класс прямоугольника 
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area (self): return self.width * self.height
     
rect = Rectangle(30, 50)
print("Rectangle area:", rect.area())   # Rectangle area: 1500