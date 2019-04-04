from shape import Shape

import math # math.pi is used in this class

class Circle(Shape):
    """ Represents a circle shape. 
    ...
    Attributes
    ----------
    radius : float
        radius of circle
    """
    def __init__(self, radius):
        super().__init__()  # calls the constructor of the Shape class
                            # (sets color to green and filled to True)
        self.__radius = radius
    
    def getRadius(self):
        """ returns radius """
        return self.__radius

    def setRadius(self, radius):
        """ sets radius """
        self.__radius = radius

    @property
    def area(self):
        """ returns area : pi*r^2"""
        return self.__radius * self.__radius * math.pi

    def getDiameter(self):
        """ returns diameter : 2r"""
        return 2 * self.__radius

    def getPerimeter(self):
        """ returns diameter : 2*pi*r"""
        return 2 * self.__radius * math.pi

    def __str__(self):
        """ returns string representation of a circle."""
        return super().__str__() + " radius: " + str(self.__radius)

    def __gt__(self, other):
        """ establishes that '>' compares radius """
        if self.__radius > other.__radius:
            return True
        else:
            return False
    
    def __lt__(self, other):
        """ establishes that '<' compares radius """
        if self.__radius < other.__radius:
            return True
        else:
            return False
    
    def __iadd__(self, other):
        """ establishes that '+=' adds to radius """
        self.__radius += other
        return self
