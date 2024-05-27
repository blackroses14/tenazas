import math

# Abstraction: Shape class is an abstract class with area() and perimeter() as abstract methods
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

# Encapsulation: Each shape class encapsulates its specific properties and methods

# Inheritance: Circle, Rectangle, Triangle, and Square inherit from the appropriate classes
class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return math.pi * self._radius ** 2

    def perimeter(self):
        return 2 * math.pi * self._radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def area(self):
        s = (self._side1 + self._side2 + self._side3) / 2
        return math.sqrt(s * (s - self._side1) * (s - self._side2) * (s - self._side3))

    def perimeter(self):
        return self._side1 + self._side2 + self._side3

# Polymorphism: Square class inherits from Rectangle, demonstrating polymorphism
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)  # Calling the constructor of the parent class (Rectangle)

# Creating objects
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5), Square(4)]

# Displaying information using polymorphism
for shape in shapes:
    print("\n" + type(shape).__name__ + ":")
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

