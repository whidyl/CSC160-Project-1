
from shape import Shape
class Rectangle(Shape):
    """ Represents a Rectangle shape. 
    ...
    Attributes
    ----------
    width : float
        width of rectangle.
    height : float
        height of rectangle.
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def getWidth(self):
        """ returns width """
        return self.__width

    def getHeight(self):
        """ returns height """
        return self.__height

    def setWidth(self, value):
        """ sets width """
        self.__width = value

    def setHeight(self, value):
        """ sets height """
        self.__height = value
    
    def getArea(self):
        """ returns area of rectangle : w*h """
        return(self.getHeight() * self.getWidth())
    
    def getPerimeter(self):
        """ returns perimeter of rectangle : 2w + 2h """
        return(self.getHeight()*2 + self.getWidth()*2)


    
