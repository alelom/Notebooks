"""
Implement a class to represent a Shape object.
Implement a constructor to set the centre of the shape
with 2 co-ordinates, (x,y)
Implement methods as follows:

    shift(x,y) which shifts the centre by given x and y deltas

    aligned(Shape) which checks if this shape has the
    same centre as the given shape. Return True if it is aligned,
    and False if it is not aligned

    has_area() which returns False because for a general shape
    area undefined

Implement a class to represent a Rectangle object, which inherits
from the Shape object.
Implement a constructor to set the centre of the rectangle
with 2 co-ordinates and the length of the sides as (x,y,sideXlen,sideYlen)
Implement methods as follows:

    has_area() which returns True
    area() which returns the area of the rectangle

Implement a class to represent a Square object, which inherits
from the Rectangle object.
Implement a constructor to set the centre of the square
with 2 co-ordinates and the length of the sides as (x,y,lenSide)

Implement a class to represent a Circle object, which inherits
from the Shape object.
Implement a constructor to set the centre of the circle
with 2 co-ordinates and the radis as (x,y,radius)
Implement methods as follows:

    has_area() which returns True
    area() which returns the area of the circle

Write code to test your classes
"""
import math

class Shape:
    def __init__(self,x,y):
        self._x=x
        self._y=y
    def shift(self,x,y):
        self._x += x
        self._y += y
    def aligned(self,shape):
        if self._x == shape._x and self._y == shape._y:
            return True
        else:
            return False        
    def has_area(self):
        return False
    
class Rectangle(Shape):
    def __init__(self,x, y, sideXlen, sideYlen):
        self._sideXlen = sideXlen
        self._sideYlen = sideXlen
        super().__init__(x,y)        
    def has_area(self):
        return True
    def area(self):
        return(self._sideXlen*self._sideYlen)

class Square(Rectangle):
    def __init__(self,x,y,lenSide):
        super().__init__(x,y,lenSide,lenSide)

class Circle(Shape):
    def __init__(self,x,y,radius):
        self._radius=radius
        super().__init__(x,y)
    def has_area(self):
        return True
    def area(self):
        return self._radius**2*math.pi

