from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return round(2 * 3.14 * self.radius,2)
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
# Example usage
circle = Circle(5)
rectangle = Rectangle(4, 6)
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")