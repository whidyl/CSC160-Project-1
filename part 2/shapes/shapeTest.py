from circle import Circle
from rectangle import Rectangle
from triangle import RightTriangle

def main():
    # circle test
    radius = 25
    someCircle = Circle(radius)
    someCircle.setColor("blue")
    
    otherCircle = Circle(50)
    someCircle += 33
    print(someCircle)

    print(someCircle.getColor())
    someCircle.setColor("blue")  # calls the setColor function inherited from the Shape class
    print(someCircle)   # calls the __str__() function
    print(someCircle > otherCircle)
    someCircle.__dict__["_Shape__color"] = "blue"
    print(someCircle.getColor())
    print(someCircle.area)
    print(someCircle.__dir__())
    print()

    # test rectangle
    myRect = Rectangle(4, 8)
    myRect.setWidth(20)
    print("area: " + str(myRect.getArea()))
    print("perimeter: " + str(myRect.getPerimeter()))

    # test triangle
    myTriangle = RightTriangle(5,12,13)
    print(myTriangle)
    print("Area: " + str(myTriangle.getArea()))
    print("Perimeter: " + str(myTriangle.getPerimeter()))
main()