class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
def calculate_area(shape):
    if not isinstance(shape, Shape):
        raise TypeError("Expected an instance of Shape or its subclass")
    return shape.area()

# Example usage
if __name__ == "__main__":
    circle = Circle(5)
    square = Square(4)
    rectangle = Rectangle(3, 6)

    print("Circle area:", calculate_area(circle))
    print("Square area:", calculate_area(square))
    print("Rectangle area:", calculate_area(rectangle))
    
