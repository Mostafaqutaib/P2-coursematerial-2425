import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def perimeter(self):
        pass
    
    @property
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    @property
    def length(self):
        return self._length
    
    @property
    def width(self):
        return self._width
    
    @property
    def perimeter(self):
        return 2 * (self._length + self._width)
    
    @property
    def area(self):
        return self._length * self._width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    @property
    def side(self):
        return self._length

class Ellipse(Shape):
    def __init__(self, major_radius, minor_radius):
        self._major_radius = major_radius
        self._minor_radius = minor_radius
    
    @property
    def major_radius(self):
        return self._major_radius
    
    @property
    def minor_radius(self):
        return self._minor_radius
    
    @property
    def perimeter(self):
        raise NotImplementedError("No simple formula for ellipse perimeter")
    
    @property
    def area(self):
        return math.pi * self._minor_radius * self._major_radius

class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius, radius)
    
    @property
    def radius(self):
        return self._major_radius
    
    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    @property
    def area(self):
        return math.pi * self.radius * self.radius