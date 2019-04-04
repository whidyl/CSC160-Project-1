from shape import Shape

class RightTriangle(Shape):
    """ Represents a triangle with a 90 degree angle. 
    ...
    Attributes
    ----------
    side1 : float
        adjacent side of triangle
    side2 : float
        opposite side of triangle
    side 3 : float
        hypotenuse side of triangle (must follow pathagorean theorum.)
    """
    def __init__(self, side1, side2, side3):
        """ 
        Raises an exception if side data cannot make a right triangle.
        """
        super().__init__()
        if not (side1*side1 + side2*side2) == side3*side3:
            raise Exception("Specified triangle widths cannot make a right triangle.")
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        
    def getSide1(self):
        """ Returns side1 """
        return self.__side1
    
    def getSide2(self):
        """ Returns side1 """
        return self.__side2
    
    def getSide3(self):
        """ Returns side1 """
        return self.__side3

    def setSide1(self, value):
        """ Sets side1 """
        self.__side1 = value
    
    def setSide2(self, value):
        """ Sets side2 """
        self.__side2 = value
    
    def setSide3(self, value):
        """ Sets side3 """
        self.__side3 = value
    
    def getArea(self):
        """ returns area of triangle : (a+b)/2 """
        return(self.getSide1()*self.getSide2())/2
    
    def getPerimeter(self):
        """ returns perimeter of triangle : (a+b+c) """
        return float(self.getSide1() + self.getSide2() + self.getSide3())
    
    def __str__ (self):
        """ returns a string representation of the triangle """
        return super().__str__() + "    side 1: " + str(self.getSide1()) + "    side 2: " + str(self.getSide2()) + "    side 3: " + str(self.getSide3())
    
